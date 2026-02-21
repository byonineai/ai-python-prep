'''
9-1. Restaurant: Make a class called Restaurant .
The __init__() method for Restaurant should store two attributes:
a restaurant_name and a cuisine_type . Make a method called describe_restaurant()
that prints these two pieces of information, and a method called open_restaurant()
that prints a message indicating that the restaurant is open .
Make an instance called restaurant from your class .
Print the two attributes individually, and then call both methods .
'''

class Restaurant():
  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    print(f"{self.restaurant_name} - {self.cuisine_type}")

  def open_restaurant(self):
    print("The restaurant is open!")

restaurant = Restaurant("Brios","Italian")
restaurant1 = Restaurant("Olive Garden","Italian")
restaurant2 = Restaurant("maggiano's","Italian")

print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)

restaurant1.describe_restaurant()
restaurant1.open_restaurant()


print(restaurant2.restaurant_name)
print(restaurant2.cuisine_type)

restaurant2.describe_restaurant()
restaurant2.open_restaurant()