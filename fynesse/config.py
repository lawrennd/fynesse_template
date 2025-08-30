import os
from typing import Any, Dict
import yaml

default_file: str = os.path.join(os.path.dirname(__file__), "defaults.yml")
local_file: str = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "machine.yml")
)
user_file: str = "_config.yml"

config: Dict[str, Any] = {}

if os.path.exists(default_file):
    with open(default_file) as file:
        config.update(yaml.load(file, Loader=yaml.FullLoader))

if os.path.exists(local_file):
    with open(local_file) as file:
        config.update(yaml.load(file, Loader=yaml.FullLoader))

if os.path.exists(user_file):
    with open(user_file) as file:
        config.update(yaml.load(file, Loader=yaml.FullLoader))

if config == {}:
    raise ValueError(
        "No configuration file found at either "
        + user_file
        + " or "
        + local_file
        + " or "
        + default_file
        + "."
    )

for key, item in config.items():
    if item is str:
        config[key] = os.path.expandvars(item)
