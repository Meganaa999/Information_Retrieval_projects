input_query=input("search here: ")
query=set(())
#print(query)
import json
import nltk
#don'ynltk.download('wordnet')
import json
import re
import string
from PyDictionary import PyDictionary
dictionary=PyDictionary()

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

score_final={}
def find_rank_doc(query):
    with open("./score_per_word.json") as data:
        score_list = json.load(data)
    cnt=0
    for term in query:
        if term in score_list:
            #sorted_list=sorted(score_list[term],key=score_list[term].get,reverse=True)
            k=0
            #term2="legend"
            #print(score_list[term]+score_list[term2])
            for i in score_list[term]:
                #print(score_list[term][i])
                if cnt==0:

                    score_final[k]=score_list[term][i]
                else:
                    score_final[k]+=score_list[term][i]
                k+=1
        cnt+=1

     # Dumping the created vocabulary into a json for further use
    with open("./final_doc_scores_after_query.json", 'w') as file1:
        json.dump(score_final, file1)    

def findtop10():
    with open("./final_doc_scores_after_query.json") as data:
        score_list = json.load(data)
    sorted_list=sorted(score_list,key=score_list.get,reverse=True)
    #print(sorted_list)
    print("docs ranked as follows:")
    for i in sorted_list[:10]:
        print(i)








for w in query:
    print (dictionary.meaning(w))

print(query)
find_rank_doc(query)
findtop10()
    


