from dataclasses import dataclass
from dataclass.config.commands import DataclassConfigCommands
from dataclass.config.repository import DataclassConfigRepository
from dataclass.config.settings import DataclassConfigSettings


@dataclass
class DataclassConfig:
    settings: DataclassConfigSettings
    repository: DataclassConfigRepository
    commands: DataclassConfigCommands
