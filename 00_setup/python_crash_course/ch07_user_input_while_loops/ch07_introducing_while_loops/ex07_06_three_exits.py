# 7-6 (2) Active variable

active = True

while active:
    age_input = input("Enter your age (or 'quit' to stop): ").lower()

    if age_input == "quit":
        active = False
    else:
        age = int(age_input)

        if age < 3:
            price = 0
        elif age <= 12:
            price = 10
        else:
            price = 15

        if price == 0:
            print("Your ticket is free!")
        else:
            print(f"Your ticket costs ${price}.")
