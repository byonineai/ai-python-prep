# import pizza
#from module_name import function_name as fn
from pizza import make_pizza as mp

# Using as to Give a Module an Alias
# import pizza as p
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms','green peppers', 'extra cheese')

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing Specific Functions
# You can also import a specific function from a module. Here’s the general syntax for this approach:
# from module_name import function_name
# You can import as many functions as you want from a module by sepa-
# rating each function’s name with a comma:
# from module_name import function_0, function_1, function_2
# The making_pizzas.py example would look like this if we want to import
# just the function we’re going to use:
# from pizza import make_pizza
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Importing All Functions in a Module
# You can tell Python to import every function in a module by using the aster- isk (*) operator:
# from pizza import *
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')