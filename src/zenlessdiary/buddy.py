from typing import Dict

from src.client import client
from .url import buddy_url
from .weapon import get_all_weapons_links
from ..raw_data.buddy import all_buddy_en_map, dump_buddy


async def get_buddy_html() -> str:
    return await client.get(buddy_url)


def apply_image_to_buddy(buddy_list: Dict[str, str]):
    for name, image in buddy_list.items():
        if ava := all_buddy_en_map.get(name.lower()):
            ava.icon = image


def notice_none():
    if names := [value.name for value in all_buddy_en_map.values() if not value.icon]:
        print(f"未获取到邦布图片资源：{names}")


async def main():
    html = await get_buddy_html()
    buddy = get_all_weapons_links(html)
    apply_image_to_buddy(buddy)
    await dump_buddy()
    notice_none()
