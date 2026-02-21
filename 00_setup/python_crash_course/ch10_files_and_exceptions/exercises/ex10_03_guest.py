'''
10-3. Guest: Write a program that prompts the user for their name .
When they respond, write their name to a file called guest.txt .
'''
from pathlib import Path

filename = Path(__file__).with_name("guest.txt")

name = input("Please enter your name:")

with open(filename,'w') as file_object:
  file_object.write(name)