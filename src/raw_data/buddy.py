import asyncio

from typing import Dict, List

import aiofiles
import ujson

from models.buddy import Buddy
from path import buddy_path
from src.raw_data.base_data import get_base_data
from src.raw_data.url import text_map, buddy_config

all_buddy: List[Buddy] = []


async def parse_config_to_buddy(
    text_map_data: Dict[str, str], config: Dict[str, str]
) -> Buddy:
    bid = config["HBKDOIKGNDE"]
    name = text_map_data[config["DIIDBBGLDOL"]]
    name_en = text_map_data[config["LAFKHMCKNIO"]]
    return Buddy(
        id=bid,
        name=name,
        name_en=name_en,
    )


async def fetch_buddy() -> List[Buddy]:
    global all_buddy
    text_map_data = await get_base_data(text_map)
    data = await get_base_data(buddy_config)
    tasks = [parse_config_to_buddy(text_map_data, i) for i in data["GMNCBMLIHPE"]]
    datas: List[Buddy] = await asyncio.gather(*tasks)
    all_buddy = datas
    return all_buddy


async def dump_buddy():
    data = [avatar.dict() for avatar in all_buddy]
    data.sort(key=lambda x: x["id"])
    async with aiofiles.open(buddy_path, "w", encoding="utf-8") as f:
        await f.write(ujson.dumps(data, indent=4, ensure_ascii=False))


async def main():
    await fetch_buddy()
    await dump_buddy()
