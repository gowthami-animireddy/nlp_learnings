#  Practise project :Tokenizer in Streamlit


# goal: build a tokenizer app in streamlit to:
# accept user input
# display:
# number of tokens
# list of tokens
# most frequent tokens


import streamlit as st
from collections import Counter
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
st.title("Text Tokenizer App")

text = st.text_area("Enter your text here:")

if st.button("Tokenize"):
    tokens = word_tokenize(text)

    st.write("Number of Tokens:", len(tokens))
    st.write("List of Tokens:", tokens)

    token_freq = Counter(tokens)
    st.write("Most Frequent Tokens:", token_freq.most_common(3))

