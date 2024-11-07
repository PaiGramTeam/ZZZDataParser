from typing import Dict

from bs4 import BeautifulSoup

from models.enums import ZZZRank
from src.client import client
from src.prydwen.url import base_data_url, buddy_url
from src.zenlessdiary.weapon import Weapon as Buddy
from src.hakush.buddy import all_buddy_en_map, dump_buddy


async def get_buddies_html() -> str:
    return await client.get(buddy_url)


def get_all_buddies_links(html: str) -> Dict[str, Buddy]:
    soup = BeautifulSoup(html, "lxml")
    ch = soup.find("div", {"class": "zzz-cards"})
    chs = ch.children
    data = {}
    rank_map = {ZZZRank.A: "rarity-A", ZZZRank.S: "rarity-S"}
    for div in chs:
        if not div.text.strip():
            continue
        div2 = div.find("div", {"class": "zzz"})
        div2_class = div2.get("class")
        rank = next((k for k, v in rank_map.items() if v in div2_class), ZZZRank.NULL)
        name = div.find("span", {"class": "emp-name"}).text.strip()
        images = div.find_all("img")
        url = next((img.get("data-src") for img in images if img.get("data-src")), None)
        link = str(base_data_url / url)
        data[name] = Buddy(
            name=name,
            image=link,
            rank=rank,
        )
    return data


def apply_image_to_buddies(buddies: Dict[str, Buddy]):
    for name, buddy in buddies.items():
        if ava := all_buddy_en_map.get(name.lower()):
            ava.icon = buddy.image
            ava.rank = buddy.rank


async def main():
    # html = await get_buddies_html()
    # buddies = get_all_buddies_links(html)
    # apply_image_to_buddies(buddies)
    await dump_buddy()
