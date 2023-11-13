from pipeline.transform.transformer import Transformer
import json
import yaml
from pathlib import Path


with open("data/txt/south_sudan_acled.txt", "r") as f:
    text = [line for line in f.readlines()]

config = yaml.safe_load(Path("config.yaml").read_text())

t = Transformer(config=config["transform"])
result = []
for line in text:
    result.append(t.process(line))

with open("output.txt", "w") as f:
    f.write(json.dumps(result, indent=4))
