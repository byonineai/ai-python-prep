'''
9-4. Number Served: Start with your program from Exercise 9-1 (page 166) . Add an attribute called number_served with a default value of 0 . Create an instance called restaurant from this class . Print the number of customers the restaurant has served, and then change this value and print it again .
Add a method called set_number_served() that lets you set the number of customers that have been served . Call this method with a new number and print the value again .
Add a method called increment_number_served() that lets you increment the number of customers who’ve been served . Call this method with any num- ber you like that could represent how many customers were served in, say, a day of business .
'''
'''
1. Add attribute called number_served with default value 0
2. Create instance called restaurant
3. Add a method called set_number_served() - let's you set the number of customers that have been served
4. Add a method called increment_number_served() that lets you set the number of customers that have been served
'''

class Restaurant():
  def __init__(self, restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0

  def describe_restaurant(self):
    print(f"{self.restaurant_name} - {self.cuisine_type} - number served {self.number_served}")

  def open_restaurant(self):
    print("The restaurant is open!")

  def set_number_served(self, number):
    self.number_served = number
    print(f"The number served is {self.number_served}")

  def increment_number_served(self, number):
    self.number_served +=number
# Create an instance called restaurant
restaurant = Restaurant("Casa Marcelo", "Brazilian")

# Print default number served
print("Number served:", restaurant.number_served)

# Change the value directly and print again
restaurant.number_served = 15
print("Number served:", restaurant.number_served)

# Use set_number_served() and print again
restaurant.set_number_served(40)
print("Number served:", restaurant.number_served)

# Use increment_number_served() and print again
restaurant.increment_number_served(25)
print("Number served:", restaurant.number_served)