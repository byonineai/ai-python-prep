'''
Icecream stand class inherits Restaurant
'''

class Restaurant():
  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    print(f"{self.restaurant_name} - {self.cuisine_type}")

  def open_restaurant(self):
    print("The restaurant is open!")

class IceCreamStand(Restaurant):
  def __init__(self,restaurant_name, cuisine_type,flavors):
    super().__init__(restaurant_name,cuisine_type)
    self.flavors = flavors
  def display_flavors(self):
    print("Available flavors:")
    for flavor in self.flavors:
      print(f"- {flavor}")

icecream = IceCreamStand(
    "Marcelo's Ice Cream",
    "Dessert",
    ["Chocolate", "Vanilla", "Strawberry"]
)
icecream.display_flavors()
