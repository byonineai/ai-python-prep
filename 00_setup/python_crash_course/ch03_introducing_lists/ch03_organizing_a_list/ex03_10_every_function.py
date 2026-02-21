# 3-10 Every Function (Chapter 3)

cities = ["Fortaleza", "Lisbon", "Rome", "Amsterdam", "Berlin"]
print("Original:", cities)

# len()
print("Length:", len(cities))

# Access by index
print("First city:", cities[0])
print("Last city:", cities[-1])

# Modify an element
cities[0] = "São Paulo"
print("After modify:", cities)

# append()
cities.append("Tokyo")
print("After append:", cities)

# insert()
cities.insert(1, "Paris")
print("After insert:", cities)

# del statement
del cities[2]
print("After del index 2:", cities)

# pop() - removes last by default
removed = cities.pop()
print("Popped (last):", removed)
print("After pop last:", cities)

# pop(index)
removed = cities.pop(1)
print("Popped (index 1):", removed)
print("After pop index 1:", cities)

# remove(value)
cities.remove("Berlin")
print("After remove 'Berlin':", cities)

# sorted() - temporary sort (doesn't change original)
print("sorted() copy:", sorted(cities))
print("After sorted(), still:", cities)

# sort() - permanent sort (changes list)
cities.sort()
print("After sort():", cities)

# sort(reverse=True)
cities.sort(reverse=True)
print("After sort(reverse=True):", cities)

# reverse() - reverse order permanently (in-place)
cities.reverse()
print("After reverse():", cities)

# Slicing
print("First 2 cities:", cities[:2])
print("Middle cities:", cities[1:3])
print("Last 2 cities:", cities[-2:])

# Looping
print("\nLoop:")
for city in cities:
    print("-", city)

# Copying a list (important!)
cities_copy = cities[:]  # or list(cities)
print("\nCopy:", cities_copy)

# Clear the list (not required in Ch.3, but useful)
cities.clear()
print("After clear():", cities)