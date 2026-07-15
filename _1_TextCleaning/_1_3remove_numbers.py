
# method 2
# using isdigit

text="i have 2 dogs"
cleaned = ''.join( c for c in text if not c.isdigit())
print(cleaned)


# method 2 
# using re

import re
text="i have 2 dogs"
cleaned=re.sub(r'\d+','',text)
print(cleaned)



# method 3
# usingtoken filtering

text="i have 2 dogs"
words=text.split()
filtered=[w for w in words if not w.isnumeric()]
print(filtered)