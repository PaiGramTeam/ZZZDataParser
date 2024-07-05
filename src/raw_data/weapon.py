import asyncio

from typing import Dict, List

import aiofiles
import ujson

from models.weapon import Weapon
from path import weapons_path
from src.raw_data.base_data import get_base_data
from src.raw_data.url import text_map, weapon_config, text_en_map

all_weapons: List[Weapon] = []


async def parse_config_to_weapon(
        text_map_data: Dict[str, str],
        text_en_map_data: Dict[str, str],
        config: Dict[str, str],
) -> Weapon:
    wid = config["NOJCFGOCGBI"]
    name_key = f"Item_{config['LAFKHMCKNIO']}_Name"
    name = text_map_data[name_key]
    name_en = text_en_map_data[name_key]
    desc = text_map_data[config["EIOJNNOAENK"]]
    rank = config["LAFKHMCKNIO"].split("_")[1]
    return Weapon(
        id=wid,
        name=name,
        name_en=name_en,
        description=desc,
        rank=rank,
    )


async def fetch_weapons() -> List[Weapon]:
    global all_weapons
    text_map_data = await get_base_data(text_map)
    text_en_map_data = await get_base_data(text_en_map)
    data = await get_base_data(weapon_config)
    tasks = [parse_config_to_weapon(text_map_data, text_en_map_data, i) for i in data["GMNCBMLIHPE"]]
    datas: List[Weapon] = await asyncio.gather(*tasks)
    all_weapons = datas
    return all_weapons


async def dump_weapons():
    data = [avatar.dict() for avatar in all_weapons]
    data.sort(key=lambda x: x["id"])
    async with aiofiles.open(weapons_path, "w", encoding="utf-8") as f:
        await f.write(ujson.dumps(data, indent=4, ensure_ascii=False))


async def main():
    await fetch_weapons()
    await dump_weapons()
