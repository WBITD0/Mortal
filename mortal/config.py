import toml
import os

config_file = os.environ.get('MORTAL_CFG', 'mortal/config.toml')
with open(config_file, encoding='utf-8') as f:
    config = toml.load(f)
