import json
from pathlib import Path

path = Path(__file__).with_name("username.json")

with open(path) as f_obj:
  username = json.load(f_obj)
  print("Welcome back , " + username + "!")