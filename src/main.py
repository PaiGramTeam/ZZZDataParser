from .raw_data.avatar import main as main_avatar
from .raw_data.weapon import main as main_weapon
from .raw_data.equipment_suit import main as main_equipment_suit
from .raw_data.buddy import main as main_buddy
from .zenlessdiary.avatar import main as main_avatar_src
from .zenlessdiary.weapon import main as main_weapon_src
from .zenlessdiary.equipment_suit import main as main_equipment_suit_src
from .zenlessdiary.buddy import main as main_buddy_src


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
    await main_avatar_src()
    print("获取武器资源数据")
    await main_weapon_src()
    print("获取驱动盘资源数据")
    await main_equipment_suit_src()
    print("获取邦布资源数据")
    await main_buddy_src()
