import asyncio

from typing import Dict, List

import aiofiles
import ujson

from models.avatar import Avatar
from path import avatars_path
from src.raw_data.base_data import get_base_data
from src.raw_data.url import text_map, avatar_config

all_avatars: List[Avatar] = []
all_avatars_en_map: Dict[str, Avatar] = {}


async def fetch_text_map() -> Dict[str, str]:
    return await get_base_data(text_map)


async def parse_config_to_avatar(
    text_map_data: Dict[str, str], config: Dict[str, str]
) -> Avatar:
    aid = config["HBKDOIKGNDE"]
    name = text_map_data[config["DIIDBBGLDOL"]]
    name_en = text_map_data[config["LAFKHMCKNIO"]]
    name_full = text_map_data[config["NHCHCCIAPIL"]]
    name_short = config["KPAMJPAHELG"]
    element = config["KDGGNBOFDOE"][0]
    speciality = config["FCDEDAOHMIO"]
    return Avatar(
        id=aid,
        name=name,
        name_en=name_en,
        name_full=name_full,
        name_short=name_short,
        element=element,
        speciality=speciality,
    )


async def fetch_avatars() -> List[Avatar]:
    global all_avatars, all_avatars_en_map
    text_map_data = await fetch_text_map()
    data = await get_base_data(avatar_config)
    tasks = [parse_config_to_avatar(text_map_data, i) for i in data["GMNCBMLIHPE"]]
    datas: List[Avatar] = await asyncio.gather(*tasks)
    all_avatars = datas

    all_avatars_en_map.clear()
    for avatar in all_avatars:
        all_avatars_en_map[avatar.name_en.lower()] = avatar

    return all_avatars


async def dump_avatars():
    data = [avatar.dict() for avatar in all_avatars]
    data.sort(key=lambda x: x["id"])
    async with aiofiles.open(avatars_path, "w", encoding="utf-8") as f:
        await f.write(ujson.dumps(data, indent=4, ensure_ascii=False))


async def main():
    await fetch_avatars()
    await dump_avatars()
