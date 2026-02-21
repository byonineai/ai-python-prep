"This is a string"
"This is also a string"

'I told my friend, "Python is my favorite language"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# Combining and concatenating strings

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

#Adding whitespace with tabs
print("\tPython")

#Combination

print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\tC\n\tJavascript")

#Stripping white space

favorite_language = 'python '
print(favorite_language.rstrip()) #right strip
print(favorite_language.lstrip()) #left string
print(favorite_language.strip()) #both sides strip

# #Avoid syntax errors
message = "One of Python's strengths is its diverse community."
print(message)
