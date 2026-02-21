from pathlib import Path

filename = Path(__file__).with_name("programming.txt")

# with open(filename,'w') as file_object:
#   file_object.write("I love computer programming.")

#Writing multiple lines

# with open(filename,'w') as file_object:
#   file_object.write("I love computer programming.\n")
#   file_object.write("It's great!.")

#Append to a file

with open(filename,'a') as file_object:
  file_object.write("I love computer programming.\n")
  file_object.write("It's great!.")
