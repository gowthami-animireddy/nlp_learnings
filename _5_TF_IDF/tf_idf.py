

from sklearn.feature_extraction.text import TfidfVectorizer
documents = [
    "The cat sat on the mat",
    "The dog played in the park",
    "Cats and dogs are great pets"]
vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')
X = vectorizer.fit_transform(documents)
print("Words:",vectorizer.get_feature_names_out())
print("\nTF-IDF Matrix:\n",X.toarray())
