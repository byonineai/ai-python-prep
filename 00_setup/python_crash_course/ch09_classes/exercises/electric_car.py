from car import Car
from battery import Battery
class ElectricCar(Car):
  '''Represent aspects of a car, specific to eletric vehicles'''

  def __init__(self, make, model, year):
    '''Initialize attributes of the parent class.'''
    super().__init__(make,model,year)
    self.battery = Battery() #Battery instance created automatically
  #Overriding parent method
  def fill_gas_tank(self):
    '''Electric cars don't have gas tanks.'''
    print("This car does not need a gas tank!")

  def describe_battery(self):
    '''Print a statement describing the battery size.'''
    print("This car has a " + str(self.battery_size) + "-kwh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()