favorite_places = {
  'Marcelo':['Portugal','Italy','Maui'],
  'Andreia':['Holland','Spain','Rio']
}

for person, places in favorite_places.items():
  print(f"{person} favorite places are {', '.join(places)}.")