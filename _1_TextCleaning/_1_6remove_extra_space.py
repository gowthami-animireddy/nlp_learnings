text="Hello   world"
cleaned=''.join(text.split())
print(cleaned)



import re
text="Heloo   nllp"
cleaned= re.sub(r'\s+','',text)
print(cleaned)