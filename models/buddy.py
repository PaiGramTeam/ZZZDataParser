from pydantic import BaseModel


class Buddy(BaseModel):
    id: int
    """"邦布ID"""
    name: str
    """名称"""
    name_en: str
    """英文名称"""
    icon: str = ""
    """图标"""
