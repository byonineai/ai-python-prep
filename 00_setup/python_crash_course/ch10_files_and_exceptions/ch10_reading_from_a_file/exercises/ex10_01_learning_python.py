# 10-1. Learning Python

from pathlib import Path

path = Path(__file__).with_name("learning_python.txt")

print("Read the entire file ===")
contents = path.read_text()
print(contents)

print("Loop over the file object ===")
with path.open() as file_object:
    for line in file_object:
        print(line.rstrip())

print("Store lines in a list and use them outside the with block ===")
with path.open() as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace('Python','C'))