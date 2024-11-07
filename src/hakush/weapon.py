import asyncio

from typing import Dict, List

import aiofiles
import ujson

from models.enums import ZZZRank
from models.weapon import Weapon
from path import weapons_path
from src.hakush.base_data import get_base_data
from src.hakush.url import weapon_config, ui_url

all_weapons: List[Weapon] = []
all_weapons_en_map: Dict[str, Weapon] = {}


async def parse_config_to_weapon(
    _wid: str,
    config: Dict[str, str],
) -> Weapon:
    wid = int(_wid)
    name = config["CHS"]
    name_en = config["EN"]
    desc = config["desc"]
    icon = str(ui_url / f"{config['icon']}.webp") if config.get("icon") else None
    rank = ZZZRank.get_rank(int(config["rank"]) + 1)
    return Weapon(
        id=wid,
        name=name,
        name_en=name_en,
        description=desc,
        icon=icon,
        rank=rank,
    )


async def fetch_weapons() -> List[Weapon]:
    global all_weapons, all_weapons_en_map
    data = await get_base_data(weapon_config)
    tasks = [parse_config_to_weapon(k, i) for k, i in data.items()]
    datas: List[Weapon] = await asyncio.gather(*tasks)
    all_weapons = datas

    all_weapons_en_map.clear()
    for weapon in all_weapons:
        all_weapons_en_map[weapon.name_en.lower()] = weapon

    return all_weapons


async def dump_weapons():
    data = [avatar.dict() for avatar in all_weapons]
    data.sort(key=lambda x: x["id"])
    async with aiofiles.open(weapons_path, "w", encoding="utf-8") as f:
        await f.write(ujson.dumps(data, indent=4, ensure_ascii=False))


async def main():
    await fetch_weapons()
    await dump_weapons()
