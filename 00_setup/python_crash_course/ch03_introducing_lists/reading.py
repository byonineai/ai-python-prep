# #List
# #Ordered and can cootain duplicates

# bicycles = ['trek','cannondale','redline','specialized']

# print(bicycles)

# #Accessing

# print(bicycles[0].title()) #Chaining being used

# #Access last element
# print(bicycles[-1])

# message = "My first bycicle ws a " + bicycles[0].title() + "."
# print(message)

# #Changing, adding and removing

# motorcycles = ['honda', 'yamaha','suzuki']

# print(motorcycles)


# motorcycles[0] = 'ducati'
# print(motorcycles)

# motorcycles.append('biz')
# print(motorcycles)

# new_motorcycles = []
# new_motorcycles.append('honda')
# new_motorcycles.append('yamaha')
# new_motorcycles.append('suzuki')

# print(new_motorcycles)

# bikes = []
# bikes.insert(0,'ducati')

# print(bikes)

# #Remove it
# del new_motorcycles[0]
# print(new_motorcycles)

# cars = ['Ferrari', 'Porsche', 'Honda']

# popped_car = cars.pop()

# print(popped_car)

# scooters = ['biz','vespa']

# first_owned = scooters.pop(1)
# print('The first scooter I owned was a ' + first_owned.title() + '.')

motorcycles = ['honda','yamaha','suzuki','ducati']

print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove('ducati')
print(motorcycles)
print("\n A" + too_expensive.title() + "is too expensive for me.")