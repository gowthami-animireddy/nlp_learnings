# pip install Unicode

import unicodedata
text='café résumé naïve'
cleaned=unicodedata.normalize('NFKC',text).encode('ascii','ignore').decode('utf-8')
print(cleaned)

text='élève déjà vu '
cleaned=unicodedata.normalize('NFKC',text).encode('ascii','ignore').decode('utf-8')
print(cleaned)



# method 2

# pip install unidecode

from unidecode import unidecode
text='élève déjà vu '
cleaned=unidecode(text)
print(cleaned)