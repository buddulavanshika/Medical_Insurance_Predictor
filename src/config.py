# src/config.py
import yaml
from pathlib import Path

class Config:
    def __init__(self, config_path="config.yaml"):
        self.config = self._load_config(config_path)

    def _load_config(self, config_path):
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    def __getattr__(self, name):
        if name in self.config:
            return self.config[name]
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

# Instantiate config globally for easy access
config = Config()

if __name__ == '__main__':
    # Example of how to access config values
    print(f"Target column: {config.data['target_column']}")
    print(f"Model name: {config.model['name']}")