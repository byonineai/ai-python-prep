import json
from pathlib import Path

# username = input("What is your name?")

path = Path(__file__).with_name("username.json")

# with open(path, 'w') as f_obj:
#   json.dump(username,f_obj)
#   print("We'll remember you when you come back, " + username + "|")

def greet_user():
  """Greet the user by name."""

try:
  with open(path) as f_obj:
    username = json.load(f_obj)
except FileNotFoundError:
  username = input("What is your name? ")
  with open(path,'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
else:
  print("Welcome back, " + username + "!")

greet_user()