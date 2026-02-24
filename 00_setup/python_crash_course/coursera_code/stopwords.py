stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

words = org.split()
acro = ""

for word in words:
    clean_word = word.strip(",").strip(".").strip("!").strip("?").strip(";").strip(":")
    if clean_word not in stopwords and clean_word.lower() not in [s.lower() for s in stopwords]:
        acro += clean_word[0].upper()
