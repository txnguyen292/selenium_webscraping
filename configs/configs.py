from pathlib import Path

class BASE:
    base_path = Path(__file__).resolve().parent

class CONFIGS:
    data_path = BASE.base_path / "data"
    src_path = BASE.base_path / "src"