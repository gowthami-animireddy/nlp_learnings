import re
import string
import unicodedata
import contractions
import emoji
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
text = "Heyyy!!! 👋 I'm sooo excited about this AI/ML course!!! Visit https://example.com NOW!!! 😎😎 I’ve completed 2 assignments, but honestly... I didn’t understand 100% of it 😅 — can you pls help me??? Email me @ mailto:anusha123@gmail.com ASAP!!! #learning #AI #2026 🚀🚀 "
text = text.lower()
text = contractions.fix(text)
text = re.sub(r'<.*?>', '', text)
text = re.sub(r'http\S+|www\S+', '', text)
text = emoji.replace_emoji(text, replace='')
text = ''.join(c for c in text if c not in string.punctuation)
text = ''.join(c for c in text if not c.isdigit())
text = re.sub(r'[^a-zA-Z\s]', '', text)
text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
text = " ".join(text.split())
words = word_tokenize(text)
words = [w for w in words if w not in stopwords.words('english')]

# Final output
cleaned_text = " ".join(words)

print(cleaned_text)