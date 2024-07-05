from typing import List

from pydantic import BaseModel


class WeaponIcon(BaseModel):
    id: int
    """武器ID"""
    name: str
    """名称"""
    icon: List[str]
    """图标（从小到大）"""

    @property
    def gacha(self) -> str:
        return self.icon[1]

    @property
    def icon_(self) -> str:
        return self.icon[0]
