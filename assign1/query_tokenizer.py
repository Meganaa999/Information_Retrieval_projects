#input_query=input("search here: ")
#print(query)
import json
import nltk
#don'ynltk.download('wordnet')
import json
import re
import string


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
#from textblob import Word 

def preprocessing(query):
    queryfin=set(())
    stemmer = SnowballStemmer("english")
    lemmatizer = WordNetLemmatizer()
    stop_words=set(stopwords.words('english'))

    #for line in query:
    query=query.lower()
    #print(query)
    tokenizer = nltk.RegexpTokenizer(r"\w+")
    tokens1 = tokenizer.tokenize(query)
        
        
    line_without_stopwords=[w for w in tokens1 if not w in stop_words]
    line_without_stopwords=[]
                
        #for a single word in a line remove stop words
    for w in tokens1:
        if w not in stop_words:
            line_without_stopwords.append(w)
                
    tokens2 = [stemmer.stem(token) for token in line_without_stopwords] # Stemming
    for w in tokens2:
        #v=Word(w)
        queryfin.add(w)
        v=lemmatizer.lemmatize(w)
        #print(v)
        queryfin.add(v)
    
    return queryfin


def find_rank_doc(query):
    with open("./score_per_word.json") as data:
        tf_idf = json.load(data)
    score_final={}
    cnt=0
    for term in query:
        if term in tf_idf:
            #sorted_list=sorted(score_list[term],key=score_list[term].get,reverse=True)
            k=0
            #term2="legend"
            #print(score_list[term]+score_list[term2])
            for i in tf_idf[term]:
                #print(score_list[term][i])
                if cnt==0:
                    score_final[k]=tf_idf[term][i]
                else:
                    score_final[k]+=tf_idf[term][i]
                k+=1
        cnt+=1

     # Dumping the created vocabulary into a json for further use
     
    findtop10(score_final)
    return score_final

def findtop10(score_final):
    sorted_list=sorted(score_final,key=score_final.get,reverse=True)
    #print(sorted_list)
    print("docs ranked as follows:")
    for i in sorted_list[:10]:
        print(i, score_final[i])
    



def exec(query):
    query_new=preprocessing(query)
    print(query_new)
    score_list = find_rank_doc(query_new)
    return query_new, score_list
    


