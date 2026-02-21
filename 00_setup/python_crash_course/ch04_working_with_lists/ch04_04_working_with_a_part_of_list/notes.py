#Slicing a list
players = ['charles','martina','michael','florence','eli']
print(players[0:3])

# Syntax: lst[start:stop] — includes start, excludes stop.
# First 3: lst[:3]
# Last 2: lst[-2:]
# Middle slice: lst[2:5]
# Every other element: lst[::2]
# Reverse: lst[::-1]
# Step: lst[start:stop:step]
# Assign or remove: lst[1:3] = [9,9] or del lst[1:3]
# Shallow copy: copy = lst[:]

my_list = [0,1,2,3,4,5,6]
print(my_list[:3])    # [0,1,2]
print(my_list[-2:])   # [5,6]
print(my_list[2:5])   # [2,3,4]
print(my_list[::2])   # [0,2,4,6]
print(my_list[::-1])  # [6,5,4,3,2,1,0]
copy = my_list[:]     # shallow copy
del my_list[1:3]      # removes indices 1 and 2

#Copying a list

my_foods = ['pizza', 'falafel','carrot cake']
friend_foods = my_foods[:]

