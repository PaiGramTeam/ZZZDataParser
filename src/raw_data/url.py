import base64

from src.base_url import URL

base_data_url = URL(base64.b64decode(
    "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL0RpbWJyZWF0aC9aZW5sZXNzRGF0YS9tYXN0ZXIv"
).decode("utf-8"))
text_map = base_data_url / "TextMap" / "TextMapTemplateTb.json"
avatar_config = base_data_url / "FileCfg" / "AvatarBaseTemplateTb.json"
weapon_config = base_data_url / "FileCfg" / "WeaponTemplateTb.json"
