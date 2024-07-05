from pydantic import BaseModel

from .enums import ZZZElementType, ZZZSpeciality


class Avatar(BaseModel):
    id: int
    """ 角色ID """
    name: str
    """ 中文名称 """
    name_en: str
    """ 英文名称 """
    name_full: str
    """ 中文全称 """
    name_short: str
    """ 英文简称 """
    rank: int
    """ 星级 """
    element: ZZZElementType
    """ 元素 """
    speciality: ZZZSpeciality
    """ 特性 """
    icon: str
    """ 图标 """
