# class Car():
#   ''' A simple attempt to represent a car'''
#   def __init__(self, make,model, year):
#     self.make = make
#     self.model = model
#     self.year = year

#   def get_descriptive_name(self):
#     '''Return a neatly formatted descriptive name. '''
#     long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#     return long_name.title()


# my_new_car = Car('audi','a4',2016)

# print(my_new_car.get_descriptive_name())

# Setting a default value for an attribute

# class Car():
#   def __init__(self, make, model, year):
#     self.make = make
#     self.model = model
#     self.year = year
#     self.odometer_reading = 0

#   def get_descriptive_name(self):
#     '''Return a neatly formatted descriptive name. '''
#     long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#     return long_name.title()

#   def read_odomoter(self):
#     """Print a statemtent showing the car's mileage"""
#     print("This car has " + str(self.odometer_reading) + " miles on it.")

# my_new_car = Car('audi','a4',2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odomoter()

#Modifying Attribute values

class Car():
  def __init__(self,make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer = 0
    self.miles = 0
    self.odometer_reading = 0

  def get_descriptive_name(self):
    long_name = str(self.year)
    return long_name.title()

  def read_odometer(self):
    print("This car has " + str(self.odometer_reading) + " miles on it.")

  def update_odometer(self,mileage):
    self.odometer = mileage

  def increment_odometer(self,miles):
    self.odometer_reading += miles

my_new_car = Car('audi','a4',2016)
my_new_car.odometer_reading = 23
my_new_car.update_odometer(23)
my_new_car.increment_odometer(100)
my_new_car.read_odometer()