import asyncio

from typing import Dict, List

import aiofiles
import ujson

from models.avatar import Avatar
from models.enums import ZZZRank, ZZZElementType
from path import avatars_path
from src.hakush.base_data import get_base_data
from src.hakush.url import avatar_config, ui_url

all_avatars: List[Avatar] = []
all_avatars_en_map: Dict[str, Avatar] = {}
all_extra_avatars_map: Dict[str, List[str]] = {
    "jane": ["jane doe"],
}


async def parse_config_to_avatar(_aid: str, config: Dict[str, str]) -> Avatar:
    aid = int(_aid)
    name = config["CHS"]
    name_en = config["EN"]
    name_full = ""
    name_short = ""
    element = config["element"]
    if element is None:
        element = ZZZElementType.NULL
    speciality = config["type"]
    rank = ZZZRank.get_rank(int(config["rank"]) + 1) if config["rank"] else ZZZRank.NULL
    icon = config["icon"]
    gacha_icon = str(ui_url / f"{config['icon']}.webp") if icon else ""
    return Avatar(
        id=aid,
        name=name,
        name_en=name_en,
        name_full=name_full,
        name_short=name_short,
        rank=rank,
        element=element,
        speciality=speciality,
        icon=["", "", "", gacha_icon],
    )


async def fetch_avatars() -> List[Avatar]:
    global all_avatars, all_avatars_en_map
    data = await get_base_data(avatar_config)
    tasks = [parse_config_to_avatar(k, i) for k, i in data.items()]
    datas: List[Avatar] = await asyncio.gather(*tasks)
    all_avatars.clear()
    all_avatars.extend(datas)

    all_avatars_en_map.clear()
    for avatar in all_avatars:
        name_en = avatar.name_en.lower()
        all_avatars_en_map[name_en] = avatar
        if name_en in all_extra_avatars_map:
            for name in all_extra_avatars_map[name_en]:
                all_avatars_en_map[name.lower()] = avatar

    return all_avatars


async def dump_avatars():
    data = [avatar.dict() for avatar in all_avatars]
    data.sort(key=lambda x: x["id"])
    async with aiofiles.open(avatars_path, "w", encoding="utf-8") as f:
        await f.write(ujson.dumps(data, indent=4, ensure_ascii=False))


async def main():
    await fetch_avatars()
    await dump_avatars()
