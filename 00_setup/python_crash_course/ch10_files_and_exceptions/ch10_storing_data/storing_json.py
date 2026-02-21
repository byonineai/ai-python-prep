import json
from pathlib import Path

# numbers = [2, 3, 5, 7, 11, 13]

# path = Path(__file__).with_name("numbers.json")

# with path.open("w") as f:
#     json.dump(numbers, f)

# print("Wrote to:", path)

# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = Path(__file__).with_name("username.json")

try:
  with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
  username = input("What is your name?")
  with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
else:
  print("Welcome back, " + username + "!")