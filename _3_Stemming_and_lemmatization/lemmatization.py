from nltk.stem import WordNetLemmatizer
import nltk
nltk.download("wordnet")
nltk.download("omw-1.4")
lemmatizer=WordNetLemmatizer()
print(lemmatizer.lemmatize("studies",pos='v'))
print(lemmatizer.lemmatize("studies",pos='v'))
print(lemmatizer.lemmatize("better",pos='a'))