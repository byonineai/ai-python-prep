cities = {
    "Fortaleza": {
        "country": "Brazil",
        "population": 2_700_000,
        "fact": "A major coastal city in Ceará known for beaches and strong tourism.",
    },
    "Lisbon": {
        "country": "Portugal",
        "population": 545_000,
        "fact": "Built on seven hills and famous for trams and azulejo tiles.",
    },
    "Tokyo": {
        "country": "Japan",
        "population": 14_000_000,
        "fact": "One of the world's largest metropolitan areas and a global tech hub.",
    },
}

for city, info in cities.items():
    print(f"\nCity: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")