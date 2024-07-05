from pydantic import BaseModel

from .enums import ZZZRank


class Buddy(BaseModel):
    id: int
    """"邦布ID"""
    name: str
    """名称"""
    name_en: str
    """英文名称"""
    icon: str = ""
    """图标"""
    rank: ZZZRank = ZZZRank.NULL
    """ 星级 """
