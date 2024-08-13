from typing import Dict

from models.enums import ZZZRank
from src.client import client
from .url import buddy_url
from .weapon import get_all_weapons_links, Weapon as Buddy
from ..hakush.buddy import all_buddy_en_map, dump_buddy


async def get_buddy_html() -> str:
    return await client.get(buddy_url)


def apply_image_to_buddy(buddy_list: Dict[str, Buddy]):
    for name, buddy in buddy_list.items():
        if ava := all_buddy_en_map.get(name.lower()):
            if not ava.icon:
                ava.icon = buddy.image
            if (not ava.rank) or ava.rank == ZZZRank.NULL:
                ava.rank = buddy.rank


def notice_none():
    if names := [value.name for value in all_buddy_en_map.values() if not value.icon]:
        print(f"未获取到邦布图片资源：{names}")
    if names := [
        value.name for value in all_buddy_en_map.values() if value.rank == ZZZRank.NULL
    ]:
        print(f"未获取到邦布稀有度：{names}")


async def main():
    html = await get_buddy_html()
    buddy = get_all_weapons_links(html)
    apply_image_to_buddy(buddy)
    await dump_buddy()
    notice_none()
