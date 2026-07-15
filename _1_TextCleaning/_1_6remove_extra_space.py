
# method 1
text="Hello   world"
cleaned=''.join(text.split())
print(cleaned)


# method 2
# using re
import re
text="Heloo   nllp"
cleaned= re.sub(r'\s+','',text)
print(cleaned)      