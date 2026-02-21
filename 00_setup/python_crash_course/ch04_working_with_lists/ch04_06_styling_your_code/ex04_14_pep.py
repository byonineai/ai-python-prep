# for item in items:
#     print(item)

print(
    "Sorry, I can invite only two people for dinner. "
    "Thanks for understanding."
)

# print(
#     f"Sorry {removed_guest}, I can't invite you to dinner."
# )

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)

guests = ["Albert", "Marie", "Nikola", "Ada", "Alan"]

print("Sorry, I can invite only two people for dinner.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

for guest in guests:
    print(f"{guest}, you're still invited to dinner!")

del guests[0]
del guests[0]

print(guests)