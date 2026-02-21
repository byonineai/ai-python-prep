# # def greet_user():
# #   """Display a simple greeting"""
# #   print("Hello!")

# # greet_user()

# #Passing information to a function

# def greet_user(username):
#   '''Display a simple greeting'''
#   print("Hello, " + username.title() + "!")

# greet_user('jesse')

#Multiple function calls

# def describe_pet(animal_type, pet_name):
#   '''Display information about a pet.'''
#   print("I have a " + animal_type + ".")
#   print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# #Keyword arguments
# describe_pet(animal_type = "hamster", pet_name = "harry")
# describe_pet("dog", "willie")

#Default values

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')