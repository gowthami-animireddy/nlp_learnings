# Cbow

from gensim.models import Word2Vec
sentences = [["Deep","Learning","is","fun"],["Machine","Learning","is","powerful"]]
model = Word2Vec(sentences=sentences, vector_size=50,window=2,sg=0,min_count=1)
print(model.wv["Learning"])         #Represents meaning of "Learning"
print(model.wv.most_similar("Learning"))        #Words ranked by similarity score