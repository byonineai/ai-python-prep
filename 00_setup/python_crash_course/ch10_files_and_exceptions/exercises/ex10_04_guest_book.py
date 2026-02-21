'''
 10-4. Guest Book: Write a while loop that prompts users for their name .
 When they enter their name, print a greeting to the screen and add a
 line recording their visit in a file called guest_book.txt .
 Make sure each entry appears on a new line in the file .
'''
from pathlib import Path

filename = Path(__file__).with_name("guest_book.txt")

while True:
  name = input("What is your name?")
  if(name):
    with open(filename,'w') as file_object:
      file_object.write(name)
    print(f"Welcome {name}!")
    break