import base64

from src.base_url import URL

base_data_url = URL(
    base64.b64decode(
        "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0RpbWJyZWF0aC9aZW5sZXNzRGF0YS9tYXN0ZXIv"
    ).decode("utf-8")
)
text_map = base_data_url / "TextMap" / "TextMapTemplateTb.json"
text_en_map = base_data_url / "TextMap" / "TextMap_ENTemplateTb.json"
avatar_config = base_data_url / "FileCfg" / "AvatarBaseTemplateTb.json"
weapon_config = base_data_url / "FileCfg" / "WeaponTemplateTb.json"
equipment_suit_config = base_data_url / "FileCfg" / "EquipmentSuitTemplateTb.json"
buddy_config = base_data_url / "FileCfg" / "BuddyBaseTemplateTb.json"
