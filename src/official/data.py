from typing import Dict

from .url import get_square_avatar_url, get_vertical_painting_url

from ..hakush.avatar import all_avatars, dump_avatars
from ..hakush.buddy import all_buddy, dump_buddy


def apply_to_avatars():
    for avatar in all_avatars:
        avatar.icon[0] = str(get_vertical_painting_url(avatar.id))
        avatar.icon[1] = str(get_square_avatar_url(avatar.id))


def apply_to_buddy(data: Dict[str, str]):
    for buddy in all_buddy:
        key = f"bangboo_square_avatar_{buddy.id}"
        if value := data.get(key):
            buddy.square = value


async def main():
    apply_to_avatars()
    # apply_to_buddy(data)
    await dump_avatars()
    await dump_buddy()
