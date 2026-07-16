# write a function in streamlit that removes english stopwords (like "the", "is", "in", etc.) from a given text input by the user. The function should take the user's text input, tokenize it, remove the stopwords, and then display the cleaned text without the stopwords.

# cleaned tokens
# count of removed stopwords
# # hint : use nltk.corpus.stopwords 


import streamlit as st
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
st.title("Stopword Removal App")
text=st.text_area("Enter your text here:")
if st.button("Remove Stopwords"):
    tokens=word_tokenize(text)
    stop_words=set(stopwords.words('english'))
    filtered_tokens=[word for word in tokens if word.lower() not in stop_words]
    removed_count=len(tokens)-len(filtered_tokens)
    st.write("Filtered Tokens:", " ".join(filtered_tokens))
    st.write("Number of Removed Stopwords:", removed_count)