from battery import Battery
class Car():
  '''A simple attempt to represet a car.'''

  def __init__(self,make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descriptive_name(self):
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()

  def read_odometer(self):
    print("This car has " + str(self.odometer_reading) + " miles on it.")

  def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")
  def fill_gas_tank():
    print("This car needs a gas tank!")

  def increment_odometer(self, miles):
    self.odometer_reading += miles

class ElectricCar(Car):
  '''Represent aspects of a car, specific to eletric vehicles'''

  def __init__(self, make, model, year):
    '''Initialize attributes of the parent class.'''
    super().__init__(make,model,year)
    self.battery_size = 70
    self.battery = Battery() #Battery instance created automatically
  #Overriding parent method
  def fill_gas_tank(self):
    '''Electric cars don't have gas tanks.'''
    print("This car does not need a gas tank!")

  def describe_battery(self):
    '''Print a statement describing the battery size.'''
    print("This car has a " + str(self.battery_size) + "-kwh battery.")
