from pathlib import Path

data_path = Path("data")
raw_path = data_path / "raw"
data_path.mkdir(exist_ok=True)
raw_path.mkdir(exist_ok=True)

avatars_path = data_path / "avatars.json"
