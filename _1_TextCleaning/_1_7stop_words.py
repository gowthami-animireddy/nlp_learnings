# pip install nltk


# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('punkt_tab')
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# text="this is a simple nlp example"
# words=word_tokenize(text)
# filtered=[w for w in words if w.lower() not in stopwords.words('english')]
# print(filtered)


# o/p
# ['simple', 'nlp', 'example']




import spacy
nlp=spacy.load("en_core_web_sm")
text="this is a simple nlp example"
doc=nlp(text)
filtered=[token.text for token in doc if not token.is_stop]
print(filtered)