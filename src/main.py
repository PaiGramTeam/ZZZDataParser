from .hakush.avatar import main as main_avatar
from .hakush.weapon import main as main_weapon
from .hakush.equipment_suit import main as main_equipment_suit
from .hakush.buddy import main as main_buddy
from .official.data import main as main_official_data
from .zenlessdiary.weapon import main as main_weapon_src
from .zenlessdiary.equipment_suit import main as main_equipment_suit_src
from .zenlessdiary.buddy import main as main_buddy_src
from .prydwen.avatar import main as main_avatar_src_normal
from .prydwen.buddy import main as main_buddy_src_normal


async def main():
    print("获取角色数据")
    await main_avatar()
    print("获取武器数据")
    await main_weapon()
    print("获取驱动盘数据")
    await main_equipment_suit()
    print("获取邦布数据")
    await main_buddy()
    print("获取角色资源数据")
    await main_official_data()
    print("获取角色 normal 资源数据")
    await main_avatar_src_normal()
    print("获取武器资源数据")
    await main_weapon_src()
    print("获取驱动盘资源数据")
    await main_equipment_suit_src()
    print("获取邦布资源数据 1")
    await main_buddy_src_normal()
    print("获取邦布资源数据 2")
    await main_buddy_src()
