from nltk.stem import SnowballStemmer
stemmer=SnowballStemmer("english")
word=['happiness','playing','studies']
for w in word:
    print(stemmer.stem(w))
