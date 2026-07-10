# import re
# text="i love nlp 😆😆"
# cleaned=re.sub(r'[^\w\s]','',text)
# print(cleaned)


# pip install emoji

import emoji 
text="i love nlp 😆😆"
cleaned=emoji.demojize(text)
print(cleaned)