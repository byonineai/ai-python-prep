# 7-5. Movie Tickets

prompt = (
    "Enter your age to see the ticket price.\n"
    "Type 'quit' to stop: "
)

while True:
    age_input = input(prompt)

    if age_input.lower() == "quit":
        break

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