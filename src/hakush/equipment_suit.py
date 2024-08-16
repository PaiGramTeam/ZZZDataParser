import asyncio

from typing import Dict, List

import aiofiles
import ujson

from models.equipment_suit import EquipmentSuit
from path import equipment_suits_path
from src.hakush.base_data import get_base_data
from src.hakush.url import equipment_suit_config

all_equipment_suits: List[EquipmentSuit] = []
all_equipment_suits_en_map: Dict[str, EquipmentSuit] = {}


async def parse_config_to_weapon(
    _sid: str,
    config: Dict[str, Dict[str, str]],
) -> EquipmentSuit:
    sid = int(_sid)
    chs = config["CHS"]
    name = chs["name"]
    name_en = config.get("EN", {}).get("name", "")
    desc_2 = chs["desc2"]
    desc_4 = chs["desc4"]
    story = ""
    return EquipmentSuit(
        id=sid,
        name=name,
        name_en=name_en,
        desc_2=desc_2,
        desc_4=desc_4,
        story=story,
    )


async def fetch_equipment_suits() -> List[EquipmentSuit]:
    global all_equipment_suits, all_equipment_suits_en_map
    data = await get_base_data(equipment_suit_config)
    tasks = [parse_config_to_weapon(k, i) for k, i in data.items()]
    datas: List[EquipmentSuit] = await asyncio.gather(*tasks)
    all_equipment_suits = datas

    all_equipment_suits_en_map.clear()
    for item in all_equipment_suits:
        all_equipment_suits_en_map[item.name_en.lower()] = item

    return all_equipment_suits


async def dump_equipment_suits():
    data = [avatar.dict() for avatar in all_equipment_suits]
    data.sort(key=lambda x: x["id"])
    async with aiofiles.open(equipment_suits_path, "w", encoding="utf-8") as f:
        await f.write(ujson.dumps(data, indent=4, ensure_ascii=False))


async def main():
    await fetch_equipment_suits()
    await dump_equipment_suits()
