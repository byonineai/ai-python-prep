info = {
 'first_name':'Marcelo',
 'last_name': 'Salvador',
 'age': 47,
 'city': 'Orlando'
}
for key,value in info.items():
  print(key, value)

info['country'] = 'Brazil'

for key,value in info.items():
  print(key, value)