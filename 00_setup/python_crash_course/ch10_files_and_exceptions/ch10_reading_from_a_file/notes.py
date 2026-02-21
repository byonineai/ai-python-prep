# import os
# print("cwd:", os.getcwd())
from pathlib import Path

path = Path(__file__).with_name("pi_digits.txt")

with path.open() as file_object:
    contents = file_object.read()
    print(contents)