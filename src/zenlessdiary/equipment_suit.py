from typing import Dict

from src.client import client
from .url import equipment_suit_url
from .weapon import get_all_weapons_links
from ..raw_data.equipment_suit import all_equipment_suits_en_map, dump_equipment_suits


async def get_equipment_suit_html() -> str:
    return await client.get(equipment_suit_url)


def apply_image_to_equipment_suit(equipment_suits: Dict[str, str]):
    for name, image in equipment_suits.items():
        if ava := all_equipment_suits_en_map.get(name.lower()):
            ava.icon = image


def notice_none():
    if names := [
        value.name for value in all_equipment_suits_en_map.values() if not value.icon
    ]:
        print(f"未获取到驱动盘图片资源：{names}")


async def main():
    html = await get_equipment_suit_html()
    buddy = get_all_weapons_links(html)
    apply_image_to_equipment_suit(buddy)
    await dump_equipment_suits()
    notice_none()
