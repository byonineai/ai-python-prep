# def get_formatted_name(first_name, last_name):
#   '''Return a full name, neatly formatted'''
#   full_name = first_name + ' ' + last_name
#   return full_name.title()

# musician = get_formatted_name('jimi','hendrix')
# print(musician)

#Making argument optional

# def get_formatted_name(first_name, last_name, middle_name= ''):
#   '''Return a full name, neatly formatted'''
#   if middle_name:
#     full_name = first_name + ' ' + middle_name +  ' ' + last_name
#   else:
#     full_name = first_name + ' ' + last_name
#   return full_name.title()

# musician = get_formatted_name('jimi','hendrix')
# print(musician)

#Returning a dictionary

# def build_person(first_name, last_name):
#   person = {'first': first_name,'last': last_name}
#   return person

# musician = build_person('jimi','hendrix')
# print(musician)


# def build_person(first_name, last_name, age= ''):
#   person = {'first': first_name, 'last': last_name}
#   if age:
#     person['age'] = age
#   return person

# musician = build_person('jimi','hendrix', age=27)
# print(musician)

#Use a function with a while loop

def get_formatted_name(first_name, last_name):
  full_name = first_name +''+last_name
  return full_name.title()
while True:
  print("\n Please tell me your name:")
  print("(Enter 'q' at any time to quit)")

  f_name = input("First name: ")
  if f_name == 'q':
    break

  l_name = input("Last name: ")
  if l_name == 'q':
    break
  formatted_name = get_formatted_name(f_name, l_name)
  print("\nHello, "+formatted_name + "!")