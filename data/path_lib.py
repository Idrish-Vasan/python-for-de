from pathlib import Path

base_path=Path(__file__).resolve().parent.parent
data_path=base_path/'data'/'raw'

print(data_path)