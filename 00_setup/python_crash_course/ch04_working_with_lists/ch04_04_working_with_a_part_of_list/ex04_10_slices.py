my_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']

print(my_foods)
print(my_foods[:3])
print(my_foods[1:3])
print(my_foods[-3:])

pizzas = ['pepperoni','cheese','portuguese']

friend_pizzas = pizzas[:]

friend_pizzas.append("garlic")

print(friend_pizzas)
print(pizzas)

for pizza in friend_pizzas:
  print(pizza)