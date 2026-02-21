people = ['Mario','Maria','Carla','Carlos']

people[1] = 'Joao'

print(people[0] + ' you are invited to dinner.')
print(people[1] + ' you are invited to dinner.')
print(people[2] + ' you are invited to dinner.')

print("\nI've found a bigger table!\n")

people.insert(0,"Ana")
people.insert(len(people)//2,"Toca")
people.append("Marcio")
print(people)

while len(people) > 2:
  name = people.pop()
  print("Sorry you have been removed from the list -> " + name)

for name in people:
  print(name + ' you are still invited!')

del people[0]
del people[0]
print(people)
