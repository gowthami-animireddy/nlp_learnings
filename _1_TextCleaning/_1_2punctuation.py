# import string
# test="hello!!!!How are You???"
# cleaned=''.join(c for c in test if c not in string.punctuation)
# print(cleaned)


import re
text="NLP,AI & ML are amazing !!!!!"
cleaned=re.sub(r'[^\w\s]','',text)
print(cleaned)