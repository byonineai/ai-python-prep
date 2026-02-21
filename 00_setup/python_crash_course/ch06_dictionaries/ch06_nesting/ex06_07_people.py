# 6-1. Person

marcelo = {
    "first_name": "Marcelo",
    "last_name": "Salvador",
    "age": 47,
    "city": "Fortaleza",
}

andreia = {
  "first_name": "Andreia",
  "last_name": "Barros",
  "age": 35,
  "city": "Itarema"
}

rebecca = {
  "first_name": "Rebecca",
  "last_name": "Salvador",
  "age": 35,
  "city": "Itarema"
}

people = [marcelo,andreia,rebecca]

for person in people:
  for key, value in person.items():
    print(f"{key}: {value}")

# print(person["first_name"])
# print(person["last_name"])
# print(person["age"])
# print(person["city"])