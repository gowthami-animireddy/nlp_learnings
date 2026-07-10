# method 1
# using re

# import re
# text="<p> this is a paragraph <p>"
# cleaned=re.sub(r'<.*?>','',text)
# print(cleaned)


#method 2
#using beautiful soap

# pip install bs4

from bs4 import BeautifulSoup
text="<p> this is a paragraph <p>"
cleaned=BeautifulSoup(text,"html.parser").get_text()
print(cleaned)