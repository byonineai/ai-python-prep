dog = {'Marcelo':'Dog'}
cat = {'Mike':'Cat'}
lion = {'Don':'Lion'}

pets = [dog, cat, lion]

for animals in pets:
  for owner, animal in animals.items():
    print(f"{owner} is the owner of the {animal}")