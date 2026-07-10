from nltk.tokenize import sent_tokenize
text="Dr.Smith loves NLP. He works at google"
sen=sent_tokenize(text)
print(sen)

# o/p
# ['Dr.Smith loves NLP.', 'He works at google']


# method 2

doc=nlp(text)
sens=[sent.text for sent in doc.sents]
print(sens)