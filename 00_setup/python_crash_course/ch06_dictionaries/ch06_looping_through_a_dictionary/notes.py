#Looping  through a dictionary

user_0 ={
  'username':'efermi',
  'first':'enrico',
  'last':'fermi'
}

for key, value in user_0.items():
  print("\nkey " + key)
  print("Value: " + value)


#New version of python preserves dictionary order, but will use sort function here as example

favorite_languages = {
  'jen' : 'python',
  'sarah' : 'c',
  'edward' : 'ruby',
  'phil' : 'python'
}

for name in sorted(favorite_languages.keys()):
  print(name.title() + ", thank you for taking the poll.")