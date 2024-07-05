import asyncio

from typing import Dict, List

import aiofiles
import ujson

from models.equipment_suit import EquipmentSuit
from path import equipment_suits_path
from src.raw_data.base_data import get_base_data
from src.raw_data.url import text_map, equipment_suit_config

all_equipment_suits: List[EquipmentSuit] = []


async def parse_config_to_weapon(text_map_data: Dict[str, str], config: Dict[str, str]) -> EquipmentSuit:
    sid = config["HBKDOIKGNDE"]
    name = text_map_data[config["DIIDBBGLDOL"]]
    desc_2 = text_map_data[config["FIIENEOOHBE"]]
    desc_4 = text_map_data[config["JCAKNJLNPDM"]]
    story = text_map_data[config["DJJNBIOLAEC"]]
    return EquipmentSuit(
        id=sid,
        name=name,
        desc_2=desc_2,
        desc_4=desc_4,
        story=story,
    )


async def fetch_equipment_suits() -> List[EquipmentSuit]:
    global all_equipment_suits
    text_map_data = await get_base_data(text_map)
    data = await get_base_data(equipment_suit_config)
    tasks = [parse_config_to_weapon(text_map_data, i) for i in data["GMNCBMLIHPE"]]
    datas: List[EquipmentSuit] = await asyncio.gather(*tasks)
    all_equipment_suits = datas
    return all_equipment_suits


async def dump_equipment_suits():
    data = [avatar.dict() for avatar in all_equipment_suits]
    data.sort(key=lambda x: x["id"])
    async with aiofiles.open(equipment_suits_path, "w", encoding="utf-8") as f:
        await f.write(ujson.dumps(data, indent=4, ensure_ascii=False))


async def main():
    await fetch_equipment_suits()
    await dump_equipment_suits()
