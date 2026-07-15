from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
word=['playing','studies','happiness']
for w in word:
    print(stemmer.stem(w))