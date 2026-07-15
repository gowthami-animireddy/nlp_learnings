#  Fast Text

from gensim.models import FastText
sentences = [["Deep","Learning","is","fun"],["Machine","Learning","is","powerful"]]
model = FastText(sentences=sentences, vector_size=50,window=2,min_count=1)
print(model.wv["Learning"])         #Represents meaning of "Learning"
print(model.wv.most_similar("Learning"))        #Words ranked by similarity score