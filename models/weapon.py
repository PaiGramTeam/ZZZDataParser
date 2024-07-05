from pydantic import BaseModel

from models.enums import ZZZRank


class Weapon(BaseModel):
    id: int
    """"武器ID"""
    name: str
    """名称"""
    description: str
    """描述"""
    icon: str = ""
    """图标"""
    big_pic: str = ""
    """大图"""
    rank: ZZZRank
    """稀有度"""
