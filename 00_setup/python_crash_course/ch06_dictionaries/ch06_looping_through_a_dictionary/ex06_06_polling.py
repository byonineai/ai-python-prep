favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# People who should take the poll (some already responded, some haven't)
people_to_poll = ["jen", "marcelo", "phil", "anna", "sarah", "mike"]

for person in people_to_poll:
  if person in favorite_languages:
    print(f"Thanks for taking the poll, {person.title()}!")
  else:
    print(f"{person.title()}, please take the favorite languages poll!")