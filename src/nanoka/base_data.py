from pathlib import Path

import aiofiles
import ujson

from path import raw_path
from src.client import client
from .url import base_data_url, manifest_url

VERSION = "0.0"


async def init_version():
    global VERSION
    if VERSION != "0.0":
        return
    res = await client.get(manifest_url)
    data = res.json()
    VERSION = data["zzz"]["latest"]
    print("get data version: ", VERSION)


def get_real_path(url: str) -> Path:
    file_url = url.replace(f"{str(base_data_url)}/", "")
    file_path = Path(file_url)
    (raw_path / file_path.parent).mkdir(parents=True, exist_ok=True)
    return raw_path / file_path


async def get_base_data_from_file(file_path: Path):
    async with aiofiles.open(file_path, "r", encoding="utf-8") as f:
        return ujson.loads(await f.read())


async def get_base_data_from_url(url: str, file_path: Path) -> dict:
    res = await client.get(url)
    data = res.json()
    async with aiofiles.open(file_path, "w", encoding="utf-8") as f:
        await f.write(ujson.dumps(data, indent=4, ensure_ascii=False))
    return data


async def get_base_data(raw_url: str) -> dict:
    url = str(raw_url)
    file_path = get_real_path(url)
    await init_version()
    url = url.replace("VER_REPLACE", VERSION)
    if file_path.exists():
        return await get_base_data_from_file(file_path)
    return await get_base_data_from_url(url, file_path)
