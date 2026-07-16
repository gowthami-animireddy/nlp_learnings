# extend your streamlit tokenizer to:
# tokenize at sentence level
# display number of sentences
# display first and last word of user input text
# hint:
# use nltk.sent_tokenize and list indexing



import streamlit as st
from nltk.tokenize import word_tokenize, sent_tokenize
text = st.text_area("Enter your text here:")

if st.button("Analyze"):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    st.write("Number of Sentences:", len(sentences))
    st.write("First word:", words[0] if words else "")
    st.write("Last word:", words[-1] if words else "")
