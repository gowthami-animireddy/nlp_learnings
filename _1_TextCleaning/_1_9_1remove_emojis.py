import re
text="i love nlp 😆😆"
cleaned=re.sub(r'[^\w\s]','',text)
print(cleaned)

# o/p
# i love nlp 

# pip install emoji

import emoji 
text="i love nlp 😆😆"
cleaned=emoji.demojize(text)
print(cleaned)

# o/p
# i love nlp :grinning_squinting_face::grinning_squinting_face: