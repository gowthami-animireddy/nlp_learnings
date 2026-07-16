# allow the user to add their own stopwords(comma -separeted) and remove them from the text.


import streamlit as st
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

st.title(" Custom Stopword Removal")

text = st.text_area("Enter your text here:")

custom_stopwords = st.text_input("Enter your custom stopwords (comma-separated):")

if st.button("Remove Stopwords"):
    base_stopwords = set(stopwords.words('english'))
    custom_stopwords_set = [word.strip().lower() for word in custom_stopwords.split(',') if word]

    all_stopwords = base_stopwords.union(set(custom_stopwords_set))

    tokens = word_tokenize(text)
    filtered = [word for word in tokens if word.lower() not in all_stopwords]


    st.subheader("Filtered Text:")
    st.write(" ".join(filtered)) 
