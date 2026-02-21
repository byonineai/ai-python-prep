# import random
# # # A list of dictionaries

# # alien_0 = {'color':'green','points':5}
# # alien_1 = {'color':'yellow','points':10}
# # alien_2 = {'color':'red','points':15}

# # aliens = [alien_0, alien_1, alien_2]

# # for alien in aliens:
# #   print(alien)

# #Make 30 aliens

# # aliens = []
# # colors = ["red", "blue", "green", "yellow"]
# # for alien_number in range(30):
# #   new_alien = {'color': random.choice(colors), 'points':5, 'speed': 'slow'}
# #   aliens.append(new_alien)

# # for alien in aliens:
# #   print(f"Color: {alien}")

# #Store information about pizza being ordered

# pizza = {
#   'crust': 'thick',
#   'toppings': ['mushrooms','extra cheese']
# }

# # Summarize the order.
# print("You ordered a " + pizza['crust'] + "-crust pizza " +
#       "with the following toppings:")

# for topping in pizza['toppings']:
#   print("\t" + topping)

favorite_languages = {
  'jen': ['python','ruby'],
  'sarah':['c'],
  'edward':['ruby','go'],
  'phil': ['python','haskell']
}

for name,languages in favorite_languages.items():
     print("\n" + name.title() + "'s favorite languages are:")
     for language in languages:
          print("\t" + language.title())