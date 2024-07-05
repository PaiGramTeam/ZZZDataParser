from typing import Dict

from bs4 import BeautifulSoup

from src.client import client
from .url import weapons_url
from ..raw_data.weapon import all_weapons_en_map, dump_weapons


async def get_weapons_html() -> str:
    return await client.get(weapons_url)


def get_all_weapons_links(html: str) -> Dict[str, str]:
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
        data[name] = first_image
    return data


def fix_weapon(weapons: Dict[str, str]):
    weapons["Drill Rig - Red Axis"] = weapons["Drill Rig – Red Axis"]


def apply_image_to_weapon(weapons: Dict[str, str]):
    for name, image in weapons.items():
        if ava := all_weapons_en_map.get(name.lower()):
            ava.icon = image


def notice_none():
    if names := [value.name for value in all_weapons_en_map.values() if not value.icon]:
        print(f"未获取到武器图片资源：{names}")


async def main():
    html = await get_weapons_html()
    weapons = get_all_weapons_links(html)
    fix_weapon(weapons)
    apply_image_to_weapon(weapons)
    await dump_weapons()
    notice_none()
