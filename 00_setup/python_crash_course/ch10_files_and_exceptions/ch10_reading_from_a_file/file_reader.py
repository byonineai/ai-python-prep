from pathlib import Path

path = Path(__file__).with_name("pi_digits.txt")

# with path.open() as file_object:
#     for line in file_object:
#         print(line.rstrip())
    # contents = file_object.read()
    # print(contents)

#Making a list of lines from a file

with open(path) as file_object:
  lines = file_object.readlines()

for line in lines:
  print(line.rstrip())