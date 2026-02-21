from car import Car, ElectricCar
#import entire module
#import car
#import all classes from a module
# from module_name import *

'''
my_beetle = car.Car('volkswagen','beetle',2016)
my_tesla = car.ElectricCar('tesla','roadster',2016)
'''

my_beetle = Car('Volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())