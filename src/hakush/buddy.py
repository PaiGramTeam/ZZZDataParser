import asyncio

from typing import Dict, List

import aiofiles
import ujson

from models.buddy import Buddy
from models.enums import ZZZRank
from path import buddy_path
from src.hakush.base_data import get_base_data
from src.hakush.url import buddy_config

all_buddy: List[Buddy] = []
all_buddy_en_map: Dict[str, Buddy] = {}


async def parse_config_to_buddy(_bid: str, config: Dict[str, str]) -> Buddy:
    bid = int(_bid)
    name = config["CHS"]
    name_en = config["EN"]
    rank = ZZZRank.get_rank(int(config["rank"]) + 1)
    return Buddy(
        id=bid,
        name=name,
        name_en=name_en,
        rank=rank,
    )


async def fetch_buddy() -> List[Buddy]:
    global all_buddy, all_buddy_en_map
    data = await get_base_data(buddy_config)
    tasks = [parse_config_to_buddy(k, i) for k, i in data.items()]
    datas: List[Buddy] = await asyncio.gather(*tasks)
    all_buddy.clear()
    all_buddy.extend(datas)

    all_buddy_en_map.clear()
    for buddy in datas:
        all_buddy_en_map[buddy.name_en.lower()] = buddy

    return all_buddy


async def dump_buddy():
    data = [avatar.dict() for avatar in all_buddy]
    data.sort(key=lambda x: x["id"])
    async with aiofiles.open(buddy_path, "w", encoding="utf-8") as f:
        await f.write(ujson.dumps(data, indent=4, ensure_ascii=False))


async def main():
    await fetch_buddy()
    await dump_buddy()
