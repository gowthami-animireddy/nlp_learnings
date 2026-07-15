from nltk.stem import LancasterStemmer
stemmer=LancasterStemmer()
word=['happiness','playing','studies']
for w in word:
    print(stemmer.stem(w))