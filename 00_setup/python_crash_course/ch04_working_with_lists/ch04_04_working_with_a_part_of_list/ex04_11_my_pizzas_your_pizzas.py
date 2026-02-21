pizzas = ['pepperoni','cheese','portuguese']

friend_pizzas = pizzas[:]

friend_pizzas.append("garlic")

print(friend_pizzas)
print(pizzas)

for pizza in friend_pizzas:
  print(pizza)