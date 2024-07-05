import asyncio
import dataclasses
from typing import List

from bs4 import BeautifulSoup

from models.enums import ZZZRank
from src.client import client
from .url import characters_url
from ..raw_data.avatar import all_avatars_en_map, dump_avatars


@dataclasses.dataclass
class Avatar:
    name: str
    link: str
    first_image: str
    banner_image: str
    rank: ZZZRank


async def get_characters_html() -> str:
    return await client.get(characters_url)


def parse_rank(class_list: List[str]) -> ZZZRank:
    if "s" in class_list or "S" in class_list:
        return ZZZRank.S
    if "a" in class_list or "A" in class_list:
        return ZZZRank.A
    if "b" in class_list or "B" in class_list:
        return ZZZRank.B
    return ZZZRank.NULL


def get_all_characters_links(html: str) -> List[Avatar]:
    soup = BeautifulSoup(html, "lxml")
    ch = soup.find("div", {"class": "characters"})
    chs = ch.children
    data = []
    for div in chs:
        if not div.text.strip():
            continue
        name = div.find("h2").text.strip()
        link = div.find("a", {"class": "gb-container-link"}).get("href")
        image = div.find_all("img")
        first_image = image[-1].get("src")
        class_list = div.get("class")
        rank = parse_rank(class_list)
        data.append(
            Avatar(
                name=name,
                link=link,
                first_image=first_image,
                banner_image="",
                rank=rank,
            )
        )
    return data


async def get_character_banner_image(avatar: Avatar) -> None:
    html = await client.get(avatar.link)
    soup = BeautifulSoup(html.text, "lxml")
    c = soup.find("div", {"class": "hero-container"})
    if img := c.find("img", {"class": "gb-image-488c90b0"}):
        avatar.banner_image = img.get("src")


def apply_image_to_avatar(avatars: List[Avatar]):
    for avatar in avatars:
        if ava := all_avatars_en_map.get(avatar.name.lower()):
            ava.rank = avatar.rank
            ava.icon = [avatar.first_image, "", avatar.banner_image]


def notice_none():
    if names := [
        value.name
        for value in all_avatars_en_map.values()
        if not (value.icon_ and value.gacha)
    ]:
        print(f"未获取到角色图片资源：{names}")
    if names := [
        value.name
        for value in all_avatars_en_map.values()
        if value.rank == ZZZRank.NULL
    ]:
        print(f"未获取到角色稀有度：{names}")


async def main():
    html = await get_characters_html()
    avatars = get_all_characters_links(html)
    tasks = [get_character_banner_image(i) for i in avatars]
    await asyncio.gather(*tasks)
    apply_image_to_avatar(avatars)
    await dump_avatars()
    notice_none()
