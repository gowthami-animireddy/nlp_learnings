from sklearn.feature_extraction.text import CountVectorizer
sentences=['I love NlP','I love Coding']
vectorizer=CountVectorizer()
x=vectorizer.fit_transform(sentences)
print(vectorizer.get_feature_names_out())
print(x)
print(x.toarray())


# pip install scikit-learn