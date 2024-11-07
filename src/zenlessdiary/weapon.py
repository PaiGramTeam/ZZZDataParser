import dataclasses
from typing import Dict

from bs4 import BeautifulSoup

from models.enums import ZZZRank
from src.client import client
from .avatar import parse_rank
from .url import weapons_url
from ..hakush.weapon import all_weapons_en_map, dump_weapons


@dataclasses.dataclass
class Weapon:
    name: str
    image: str
    rank: ZZZRank


async def get_weapons_html() -> str:
    return await client.get(weapons_url)


def get_all_weapons_links(html: str) -> Dict[str, Weapon]:
    soup = BeautifulSoup(html, "lxml")
    ch = soup.find("div", {"class": "bangboo"})
    chs = ch.children
    data = {}
    for div in chs:
        if not div.text.strip():
            continue
        name = div.find("h2").text.strip()
        image = div.find_all("img")
        first_image = image[-1].get("src")
        class_list = div.get("class")
        rank = parse_rank(class_list)
        data[name] = Weapon(
            name=name,
            image=first_image,
            rank=rank,
        )
    return data


def fix_weapon(weapons: Dict[str, Weapon]):
    weapons["Drill Rig - Red Axis"] = weapons["Drill Rig – Red Axis"]


def apply_image_to_weapon(weapons: Dict[str, Weapon]):
    for name, weapon in weapons.items():
        if ava := all_weapons_en_map.get(name.lower()):
            ava.icon = weapon.image
            ava.rank = weapon.rank


def notice_none():
    if names := [value.name for value in all_weapons_en_map.values() if not value.icon]:
        print(f"未获取到武器图片资源：{names}")
    if names := [
        value.name
        for value in all_weapons_en_map.values()
        if value.rank == ZZZRank.NULL
    ]:
        print(f"未获取到武器稀有度：{names}")


async def main():
    # html = await get_weapons_html()
    # weapons = get_all_weapons_links(html)
    # fix_weapon(weapons)
    # apply_image_to_weapon(weapons)
    # await dump_weapons()
    notice_none()
