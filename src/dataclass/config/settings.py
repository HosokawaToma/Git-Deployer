from dataclasses import dataclass

@dataclass
class DataclassConfigSettings:
    interval_seconds: int
    log_file_path: str

