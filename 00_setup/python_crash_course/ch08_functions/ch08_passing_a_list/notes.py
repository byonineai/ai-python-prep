# #Passing a list
# def greet_users(names):
#   '''Print a simple greeting to each user in the list.'''
#   for name in names:
#     msg = "Hello, " + name.title() + "!"
#     print(msg)

#   usernames = ['hannah','ty','margot']

#   greet_users(usernames)

# S = [2,4,6,8]
# P = all(x % 2 == 0 for x in S)

# print(P)

#Modifying a list in Python

#Start with some designs that need to be printed.
# unprinted_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models = []

# #Similute printing each design, until non are left.
# #Move each design to completed_models after printing
# while unprinted_designs:
#   current_design = unprinted_designs.pop()

#   #simulate creating a 3D print from the design.
#   print("Printing model " + current_design)
#   completed_models.append(current_design)
#   completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#   print(completed_model)

#Rewrite with functions separating concerns

# def print_models(unprinted_designs, completed_models):
#   '''
#   Simulate printing each design, until none are left.
#   Move each design to completed_models after printing.
#   '''

#   while unprinted_designs:
#     current_design = unprinted_designs.pop()

#     # Simulate creating a 3D print from the design.
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)

# def show_completed_models(completed_models):
#   '''Show all the models that were printed'''
#   for completed_model in completed_models:
#     print(completed_model)

# unprinted_designs = ['iphone case','robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# Preventing a function from modifying a list

#function_name(list_name[:])

#print_models(unprinted_designs[:], completed_models)

