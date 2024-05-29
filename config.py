import json
import os

config = {

}


# print(json.dumps(config, indent=4, ensure_ascii=False))

# 如果有config.json则 load config.json

if os.path.exists("config.json"):
    with open("config.json", "r") as f:
        config = json.load(f)