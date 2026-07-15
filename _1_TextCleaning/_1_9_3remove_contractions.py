contractions = {
    "don't": "do not",
    "i'm": "i am",
    "it's": "it is"}
text = "I'm learning NLP and it's fun"
words = text.lower().split()
expanded = [contractions.get(w, w) for w in words]
cleaned = " ".join(expanded)
print(cleaned)


# pip install contractions

import contractions
text = "I'm learning NLP and it's amazing"
cleaned = contractions.fix(text)
print(cleaned)