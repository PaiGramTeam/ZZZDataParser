from src.base_url import URL

base_url = URL("https://api.hakush.in/zzz")
base_data_url = base_url / "data"
avatar_config = base_data_url / "character.json"
weapon_config = base_data_url / "weapon.json"
equipment_suit_config = base_data_url / "equipment.json"
buddy_config = base_data_url / "bangboo.json"
