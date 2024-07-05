from typing import Dict

from models.enums import ZZZRank
from src.client import client
from .url import equipment_suit_url
from .weapon import get_all_weapons_links, Weapon as EquipmentSuit
from ..raw_data.equipment_suit import all_equipment_suits_en_map, dump_equipment_suits


async def get_equipment_suit_html() -> str:
    return await client.get(equipment_suit_url)


def apply_image_to_equipment_suit(equipment_suits: Dict[str, EquipmentSuit]):
    for name, equipment_suit in equipment_suits.items():
        if ava := all_equipment_suits_en_map.get(name.lower()):
            ava.icon = equipment_suit.image
            ava.rank = equipment_suit.rank


def notice_none():
    if names := [
        value.name for value in all_equipment_suits_en_map.values() if not value.icon
    ]:
        print(f"未获取到驱动盘图片资源：{names}")
    if names := [
        value.name
        for value in all_equipment_suits_en_map.values()
        if value.rank == ZZZRank.NULL
    ]:
        print(f"未获取到驱动盘稀有度：{names}")


async def main():
    html = await get_equipment_suit_html()
    equipment_suits = get_all_weapons_links(html)
    apply_image_to_equipment_suit(equipment_suits)
    await dump_equipment_suits()
    notice_none()
