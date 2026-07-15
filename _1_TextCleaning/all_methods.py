import re
import string
import unicodedata
import contractions
import emoji
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Input text
text = "Heyyy!!! 👋 I'm sooo excited about this AI/ML course!!! Visit https://example.com NOW!!! 😎😎 I’ve completed 2 assignments, but honestly... I didn’t understand 100% of it 😅 — can you pls help me??? Email me @ mailto:anusha123@gmail.com ASAP!!! #learning #AI #2026 🚀🚀 "

# Step 1: Lowercase
text = text.lower()

# Step 2: Expand contractions
text = contractions.fix(text)

# Step 3: Remove HTML tags
text = re.sub(r'<.*?>', '', text)

# Step 4: Remove URLs
text = re.sub(r'http\S+|www\S+', '', text)

# Step 5: Remove emojis
text = emoji.replace_emoji(text, replace='')

# Step 6: Remove punctuation
text = ''.join(c for c in text if c not in string.punctuation)

# Step 7: Remove digits
text = ''.join(c for c in text if not c.isdigit())

# Step 8: Remove special characters
text = re.sub(r'[^a-zA-Z\s]', '', text)

# Step 9: Remove accents
text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

# Step 10: Remove extra spaces
text = " ".join(text.split())

# Step 11: Tokenization
words = word_tokenize(text)

# Step 12: Remove stopwords
words = [w for w in words if w not in stopwords.words('english')]

# Final output
cleaned_text = " ".join(words)

print(cleaned_text)