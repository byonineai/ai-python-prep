'''
10-5. Programming Poll: Write a while loop that asks
people why they like programming . Each time someone enters a reason,
add their reason to a file that stores all the responses .
'''
from pathlib import Path

filename = Path(__file__).with_name("responses.txt")

flag = True

while flag:
  answer = input("Why do you like programming - Enter (quit) to exit. ")
  if answer.lower() == 'quit':
    flag = False
  else:
    with open(filename,'a') as file_object:
      file_object.write(answer+"\n")
