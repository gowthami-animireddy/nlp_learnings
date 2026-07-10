import re
text="hello @#$ nlp!!"
cleaned=re.sub(r'[^a-zA-Z\s|\d+]','',text)

print(cleaned)

clean=re.sub(r'[^a-zA-Z 0-9\s]','',text)
print(clean)