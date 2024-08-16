from typing import Dict

from .url import json_url
from ..client import client

from ..hakush.avatar import all_avatars, dump_avatars
from ..hakush.buddy import all_buddy, dump_buddy


async def get_i18n_data() -> Dict[str, str]:
    return (await client.get(json_url)).json()


def apply_to_avatars(data: Dict[str, str]):
    for avatar in all_avatars:
        key = f"role_square_avatar_{avatar.id}"
        if value := data.get(key):
            avatar.icon[1] = value


def apply_to_buddy(data: Dict[str, str]):
    for buddy in all_buddy:
        key = f"bangboo_square_avatar_{buddy.id}"
        if value := data.get(key):
            buddy.square = value


async def main():
    data = await get_i18n_data()
    apply_to_avatars(data)
    apply_to_buddy(data)
    await dump_avatars()
    await dump_buddy()
