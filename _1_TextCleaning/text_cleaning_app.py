import streamlit as st
import re
import emoji
import contractions
import spacy
from nltk.corpus import stopwords
import nltk

nlp=spacy.load("en_core_web_sm")
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


important_words = ['i','am','is','are','was','were','be','been','being','have','has','had','do','does','did','not']

def clean_text(text):

    text = text.lower()

    text = contractions.fix(text)
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'S+@\S+', '', text)
    text = emoji.replace_emoji(text, replace='')
    text = re.sub(r'\d+', '', text)
    doc=nlp(text)
    words = [token.text for token in doc if not token.is_punct]
    words = [word for word in words if (word not in stop_words) or (word in important_words)]
    text = ' '.join(words)
    return" ".join(words)

st.title("Text Cleaning App")
st.set_page_config(page_title="Text Cleaning App", page_icon=":guardsman:", layout="centered")
user_input = st.text_area("Enter your text here:", height=200)

if st.button("Clean Text"):
    if user_input.strip() == "":
        st.warning("Please enter some text to clean.")
    else:
        cleaned_text = clean_text(user_input)
        st.subheader("Cleaned Text:")
        st.write(cleaned_text)


