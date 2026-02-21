class Dog():
  '''A simple attempt to model a dog.'''

  #. the self paramenter is used in the definition, passed automatically and every
  #. method call automatically calls it. A reference to the instance itself
  #. It gives the individidual instance access to the attributes and methods in the class
  def __init__(self, name, age): # runs when an instance of the class is created
    self.name = name
    self.age = age

  def sit(self):
    '''Simulate a dog sitting in response to a command'''
    print(self.name.title() + "is now sitting.")

  def roll_over(self):
    '''Simulate rolling over in response to a command.'''
    print(self.name.title() + " rolled over!")

#Making an instance

my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

#Accessing attributes

my_dog.name

#Calling methods

my_dog.sit()
my_dog.roll_over()

#Creating multiple instances

your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
