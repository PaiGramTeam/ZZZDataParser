from enum import Enum, IntEnum


class ZZZElementType(IntEnum):
    """ZZZ element type."""

    NULL = 1
    """ 空 """
    PHYSICAL = 200
    """ 物理 """
    FIRE = 201
    """ 火 """
    ICE = 202
    """ 冰 """
    ELECTRIC = 203
    """ 电 """
    ETHER = 205
    """ 以太 """


class ZZZSpeciality(IntEnum):
    """ZZZ agent compatible speciality."""

    ATTACK = 1
    """ 强攻 """
    STUN = 2
    """ 击破 """
    ANOMALY = 3
    """ 异常 """
    SUPPORT = 4
    """ 支援 """
    DEFENSE = 5
    """ 防护 """
    RUPTURE = 6
    """ 命破 """


class ZZZRank(str, Enum):
    """ZZZ Rank"""

    S = "S"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    NULL = "NULL"

    @property
    def int(self):
        value_map = {"S": 5, "A": 4, "B": 3, "C": 2, "D": 1, "NULL": 0}
        return value_map[self.value]

    @staticmethod
    def get_rank(value: int):
        value_map = {5: "S", 4: "A", 3: "B", 2: "C", 1: "D", 0: "NULL"}
        return ZZZRank(value_map[value])
