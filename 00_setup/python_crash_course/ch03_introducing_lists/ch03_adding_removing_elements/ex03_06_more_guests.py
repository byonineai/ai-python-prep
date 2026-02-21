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
