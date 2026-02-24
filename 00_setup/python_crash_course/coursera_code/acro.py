stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

words = sent.split() #explode into strings
parts = [] #empty list

for word in words:
  if word.lower() not in stopwords:
    parts.append(word[:2].upper())
acro = '. '.join(parts)

print(acro)