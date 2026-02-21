'''
9-9. Battery Upgrade: Use the final version of electric_car.py
from this section . Add a method to the Battery class called upgrade_battery() .
This method should check the battery size and set the capacity to 85 if it isn’t already .
 Make an electric car with a default battery size, call get_range() once, and then
 call get_range() a second time after upgrading the battery .
 You should see an increase in the car’s range .
'''

from car import Car
from battery import Battery
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

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.fill_gas_tank()
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()