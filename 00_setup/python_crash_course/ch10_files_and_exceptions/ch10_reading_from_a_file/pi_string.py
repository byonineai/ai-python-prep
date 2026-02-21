from pathlib import Path

path = Path(__file__).with_name("pi_digits.txt")

with open(path) as file_object:
  lines = file_object.readlines()

pi_string = ''
for line in lines:
  # pi_string += line.rstrip()
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

#Large files handling/displaying,etc
print(pi_string[:52] + "...")
print(len(pi_string))



# with path.open() as file_object:
#     for line in file_object:
#         print(line.rstrip())
    # contents = file_object.read()
    # print(contents)

#Making a list of lines from a file

# with open(path) as file_object:
#   lines = file_object.readlines()

# for line in lines:
#   print(line.rstrip())