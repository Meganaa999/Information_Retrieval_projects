input_query=input("search here: ")
query=set(())
#print(query)
import json
import nltk
#nltk.download('wordnet')
import json
import re
import string


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
#from textblob import Word 

stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()
stop_words=set(stopwords.words('english'))

#for line in query:
input_query=input_query.lower()
#print(query)
tokenizer = nltk.RegexpTokenizer(r"\w+")
tokens1 = tokenizer.tokenize(input_query)
    
    
line_without_stopwords=[w for w in tokens1 if not w in stop_words]
line_without_stopwords=[]
            
    #for a single word in a line remove stop words
for w in tokens1:
    if w not in stop_words:
        line_without_stopwords.append(w)
            
tokens2 = [stemmer.stem(token) for token in line_without_stopwords] # Stemming
for w in tokens2:
    #v=Word(w)
    query.add(w)
    v=lemmatizer.lemmatize(w)
    #print(v)
    query.add(v)
    
#for w in query:

print(query)
    


