from src.base_url import URL


json_url = URL(
    "https://fastcdn.hoyoverse.com/mi18n/nap_global/m20240410hy38foxb7k/m20240410hy38foxb7k-zh-cn.json"
)
avatar_url = URL("https://act-webstatic.hoyoverse.com/game_record/zzzv2")


def get_square_avatar_url(avatar_id: int) -> URL:
    return avatar_url / "role_square_avatar" / f"role_square_avatar_{avatar_id}.png"


def get_vertical_painting_url(avatar_id: int) -> URL:
    return (
        avatar_url
        / "role_vertical_painting"
        / f"role_vertical_painting_{avatar_id}.png"
    )
