prompt = "Please enter a pizza topping or (quit to exit)"

message = ""

while message != 'quit':
  message = input(prompt)
  print(f"You'll add {message} to your pizza.")