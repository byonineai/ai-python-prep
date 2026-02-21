#if else
# age = 17
# if age >= 18:
#   print("You are old enough to vote!")
#   print("Have you registered to vote yet?")
# else:
#   print("Sorry, you are too young to vote.")
#   print("Please register to vote as soon as you turn 18!")

#if elif else

# age = 12
# if age < 4:
#   print("Your admission cost is $0.")
# elif age < 18:
#   print("Your admission cost is $5.")
# else:
#   print("Your admission cost is $10.")

# #Use multiple elif blocks

# age = 12

# if age <= 4:
#   price = 0
# elif age < 18:
#   price = 5
# elif age < 65:
#   price = 10
# else:
#   price = 5

#Omit else

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65: price = 5

print("Your admission cost is $" + str(price) + ".")

#Testing multiple conditions

requested_toppings = ['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese")

print("\nFinished making your pizza!")