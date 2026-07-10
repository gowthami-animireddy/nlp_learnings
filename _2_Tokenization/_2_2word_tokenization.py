

# method 1
text="hello!!! i love nlp"
token=text.split()
print(token)

# ['hello!!!', 'i', 'love', 'nlp']



# method 2
# pip install nltk

import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
from nltk.tokenize import word_tokenize
text="i'm loving nlp!!!"
token=word_tokenize(text)
print(token)


# o/p
# ['i', "'m", 'loving', 'nlp', '!', '!', '!']



# method 3
# pip install spacy
import spacy
nlp=spacy.load("en_core_web_sm")
text="i'm loving nlp!!!"
doc=nlp(text)
token=[token.text for token in doc]
print(token)