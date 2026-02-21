class Battery():
  '''A simple attempt to model a battery for an electric car.'''
  def __init__(self, battery_size = 70):
    self.battery_size = battery_size

  def get_range(self):
    '''Print a statement about the range this battery provides.'''
    if self.battery_size == 70:
      range_miles = 240
    elif self.battery_size == 85:
      range_miles = 270
    else:
      range_miles = 0

    print(f"This car can go approximately {range_miles} miles on a full charge.")

  #Exercise 9-9 Addition
  def upgrade_battery(self):
    """Upgrade the battery to 85 kWh if it isn't already."""
    if self.battery_size < 85:
      self.battery_size = 85

  def describe_battery(self):
    '''Print a statement describing the battery size.'''
    print("This car has a " + str(self.battery_size) + "-kWh battery.")