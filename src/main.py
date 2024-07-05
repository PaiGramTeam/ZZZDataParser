from .raw_data.avatar import main as main_avatar
from .raw_data.weapon import main as main_weapon


async def main():
    print("获取角色数据")
    await main_avatar()
    print("获取武器数据")
    await main_weapon()
