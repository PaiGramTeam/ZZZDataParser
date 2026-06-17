from .nanoka.avatar import main as main_avatar
from .nanoka.weapon import main as main_weapon
from .nanoka.equipment_suit import main as main_equipment_suit
from .nanoka.buddy import main as main_buddy
from .official.data import main as main_official_data


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
