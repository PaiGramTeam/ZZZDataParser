from typing import Dict

from bs4 import BeautifulSoup

from src.client import client
from src.prydwen.url import base_data_url, characters_url
from src.raw_data.avatar import all_avatars_en_map, dump_avatars


async def get_characters_html() -> str:
    return await client.get(characters_url)


def get_all_characters_links(html: str) -> Dict[str, str]:
    soup = BeautifulSoup(html, "lxml")
    ch = soup.find("div", {"class": "zzz-cards"})
    chs = ch.children
    data = {}
    for div in chs:
        if not div.text.strip():
            continue
        name = div.find("span", {"class": "emp-name"}).text.strip()
        images = div.find_all("img")
        url = next((img.get("data-src") for img in images if img.get("data-src")), None)
        link = base_data_url / url
        data[name] = str(link)
    return data


def apply_image_to_avatar(avatars: Dict[str, str]):
    for name, link in avatars.items():
        if ava := all_avatars_en_map.get(name.lower()):
            ava.icon[1] = link


def notice_none():
    if names := [
        value.name for value in all_avatars_en_map.values() if not value.normal
    ]:
        print(f"未获取到角色 normal 图片资源：{names}")


async def main():
    html = await get_characters_html()
    avatars = get_all_characters_links(html)
    apply_image_to_avatar(avatars)
    await dump_avatars()
    notice_none()
