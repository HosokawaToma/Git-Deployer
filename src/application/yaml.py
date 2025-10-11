import os

import yaml

from dataclass.config import (DataclassConfig, DataclassConfigCommands,
                              DataclassConfigRepository,
                              DataclassConfigSettings)


class ApplicationYaml:
    def __init__(self, yaml_file_path: str):
        self.yaml_file_path: str = yaml_file_path
        self.yaml_data: dict | None = None
        self.settings: DataclassConfigSettings | None = None
        self.repository: DataclassConfigRepository | None = None
        self.commands: DataclassConfigCommands | None = None
        self.config: DataclassConfig | None = None
        self.load()

    def load(self) -> None:
        self._load_yaml()
        self._load_yaml_settings()
        self._load_yaml_repository()
        self._load_yaml_commands()
        self._load_yaml_config()

    def _load_yaml(self) -> None:
        if (self.yaml_file_path is None):
            raise ValueError("YAML file path is required")
        if (not os.path.exists(self.yaml_file_path)):
            raise FileNotFoundError(f"YAML file path {self.yaml_file_path} does not exist")
        with open(self.yaml_file_path, 'r') as f:
            try:
                self.yaml_data = yaml.safe_load(f)
            except yaml.YAMLError as error:
                raise ValueError(f"YAML file {self.yaml_file_path} is not valid: {error}")

    def _load_yaml_settings(self) -> None:
        if (self.yaml_data is None):
            raise ValueError("YAML data is required")
        if self.yaml_data['settings'] is None:
            raise ValueError("YAML data settings is required")
        if (not isinstance(self.yaml_data['settings'], dict)):
            raise ValueError("YAML data settings is not a dictionary")
        if self.yaml_data['settings']['interval_seconds'] is None:
            raise ValueError("YAML data settings interval_seconds is required")
        if self.yaml_data['settings']['log_file_path'] is None:
            raise ValueError("YAML data settings log_file_path is required")
        if (not isinstance(self.yaml_data['settings']['interval_seconds'], int)):
            raise ValueError("YAML data settings interval_seconds is not an integer")
        if (not isinstance(self.yaml_data['settings']['log_file_path'], str)):
            raise ValueError("YAML data settings log_file_path is not a string")
        self.settings = DataclassConfigSettings(
            interval_seconds=self.yaml_data['settings']['interval_seconds'],
            log_file_path=self.yaml_data['settings']['log_file_path']
        )

    def _load_yaml_repository(self) -> None:
        if (self.yaml_data is None):
            raise ValueError("YAML data is required")
        if (self.yaml_data['repository'] is None):
            raise ValueError("YAML data repository is required")
        if (not isinstance(self.yaml_data['repository'], dict)):
            raise ValueError("YAML data repository is not a dictionary")
        if self.yaml_data['repository']['path'] is None:
            raise ValueError("YAML data repository path is required")
        if self.yaml_data['repository']['branch'] is None:
            raise ValueError("YAML data repository branch is required")
        if (not isinstance(self.yaml_data['repository']['path'], str)):
            raise ValueError("YAML data repository path is not a string")
        if (not isinstance(self.yaml_data['repository']['branch'], str)):
            raise ValueError("YAML data repository branch is not a string")
        self.repository = DataclassConfigRepository(
            path=self.yaml_data['repository']['path'],
            branch=self.yaml_data['repository']['branch']
        )

    def _load_yaml_commands(self) -> None:
        if (self.yaml_data is None):
            raise ValueError("YAML data is required")
        if self.yaml_data['commands'] is None:
            raise ValueError("YAML data commands is required")
        if self.yaml_data['commands'] is None:
            raise ValueError("YAML data commands is required")
        if (not isinstance(self.yaml_data['commands'], list)):
            raise ValueError("YAML data commands is not a list")
        if (not all(isinstance(command, str) for command in self.yaml_data['commands'])):
            raise ValueError("YAML data commands is not a list of strings")
        self.commands = DataclassConfigCommands(
            commands=self.yaml_data['commands']
        )

    def _load_yaml_config(self) -> None:
        if self.settings is None:
            raise ValueError("YAML data settings is required")
        if self.repository is None:
            raise ValueError("YAML data repository is required")
        if self.commands is None:
            raise ValueError("YAML data commands is required")
        self.config = DataclassConfig(
            settings=self.settings,
            repository=self.repository,
            commands=self.commands
        )
