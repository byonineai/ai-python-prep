#Checking for inequality

# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#   print("Hold the anchovies")

# #Checking multiple conditions

# age_0 = 22
# age_1 = 18

# result = age_0 >= 21 and age_1 >= 21
# print(result)

requested_toppings = ['mushrooms', 'onions', 'pineapple']

food_exists = 'mushrooms' in requested_toppings

print(food_exists)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
  print(user.title() + ", you can post a response if you wish.")