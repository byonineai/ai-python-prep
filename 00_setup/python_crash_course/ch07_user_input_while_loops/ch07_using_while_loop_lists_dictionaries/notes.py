# #Using a dictionary

# unconfirmed_users = ['alice', 'brian','candace']
# confirmed_users = []

# while unconfirmed_users:
#   current_user = unconfirmed_users.pop()

#   print("Verifying user: " + current_user.title())
#   confirmed_users.append(current_user)

# #Display all confirmed users.
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#   print(confirmed_user.title())

# Removing all instances of specific values from a list

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#   pets.remove('cat')

# print(pets)

#Filling a dictionary with User Input

responses = {}

# Set it to indicate polling is active
polling_active = True

while polling_active:
  name = input("\nWhat is your name? ")
  response = input("Which mountain would you like to climb someday?")

  # Store the response in the dictionary:
  responses[name] = response

  #Find out if anyone else is going to take the poll.
  repeat = input("Would you like to let another person respond? (yes/no)")
  if repeat == 'no':
    polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
