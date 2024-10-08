from pathlib import Path

data_path = Path("data")
raw_path = data_path / "raw"
data_path.mkdir(exist_ok=True)
raw_path.mkdir(exist_ok=True)

avatars_path = data_path / "avatars.json"
weapons_path = data_path / "weapons.json"
equipment_suits_path = data_path / "equipment_suits.json"
buddy_path = data_path / "buddy.json"
