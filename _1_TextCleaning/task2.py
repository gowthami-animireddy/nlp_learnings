# after cleaning, the text : count the average word length and show the percentage of stopwords removed(is that option is selected)


import streamlit as st
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize
import re
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

st.title("Clean and Analyze Text")

text = st.text_area("Enter your text here:")

remove_stop=st.checkbox("Remove Stopwords")
lowercase=st.checkbox("Convert to Lowercase")
remove_punct=st.checkbox("Remove Punctuation")
 
if st.button("Analyse"):
    result = text
    if lowercase:
        result = result.lower()
    if remove_punct:
        result = re.sub(r'[^\w\s]', '', result)

    original_tokens = word_tokenize(text)
    cleaned_tokens = word_tokenize(result)
    if remove_stop:
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in cleaned_tokens if word.lower() not in stop_words]
        result = " ".join(filtered_tokens)
    else:
        filtered_tokens = cleaned_tokens

    word_lengths = [len(word) for word in filtered_tokens]
    avg_length = round(sum(word_lengths) / len(word_lengths), 2) if word_lengths else 0

    st.subheader("Cleaned Text:")
    st.write(result)

    st.write("Word Count:", len(filtered_tokens))
    st.write("Average Word Length:", avg_length)

    if remove_stop:
        removed =len(original_tokens) - len(filtered_tokens)
        percent =(removed /len(original_tokens)) * 100 if original_tokens else 0
        st.write("Percentage of Stopwords Removed:", round(percent, 2), "%")

    freq =Counter(filtered_tokens)
    st.write("top 3 words :",freq.most_common(3))

