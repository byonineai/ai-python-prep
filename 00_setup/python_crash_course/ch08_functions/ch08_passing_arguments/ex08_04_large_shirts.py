def make_shirt(shirt_size = "XL"):
  if shirt_size.lower() == "xl" or shirt_size.lower() == "l":
    print("I love Python.")
  else:
    print(f"the shirt's size is {shirt_size}")

make_shirt()
