# # methos 1
# using re

import re
text=" visit https://example.com for more info"
cleaned=re.sub(r'https\S+','',text)
print(cleaned)

text=" visit https://google.com for more info"
cleaned=re.sub(r'https\S+','',text)
print(cleaned)
