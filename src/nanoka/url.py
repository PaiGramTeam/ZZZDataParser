from src.base_url import URL

base_url = URL("https://static.nanoka.cc")
manifest_url = base_url / "manifest.json"
base_data_url = base_url / "zzz" / "VER_REPLACE"
avatar_config = base_data_url / "character.json"
ui_url = base_url / "assets" / "zzz"
weapon_config = base_data_url / "weapon.json"
equipment_suit_config = base_data_url / "equipment.json"
buddy_config = base_data_url / "bangboo.json"
