from pathlib import Path
filename = 'alice.txt'

path = Path(__file__).with_name("alice.txt")

# with path.open() as file_object:
#     for line in file_object:
#         print(line.rstrip())
    # contents = file_object.read()
    # print(contents)

#Making a list of lines from a file
try:
  with open(path) as file_object:
    # lines = file_object.readlines()
      lines = file_object.read()

  for line in lines:
    print(line.rstrip())
except FileNotFoundError:
  msg = "Sorry, the file  does not exist"
  print(msg)
else:
  # Count the approximate number of words in the file.
  words = lines.split()
  number_of_words = len(words)
  print("The file has about " + str(number_of_words) + " words.")