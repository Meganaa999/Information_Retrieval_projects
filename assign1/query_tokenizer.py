import os
import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

#nltk.download('wordnet')

import json
import re
import string
from PyDictionary import PyDictionary
dictionary=PyDictionary()

stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()
stop_words=set(stopwords.words('english'))

documentFiles = [f for f in os.listdir("./corpus_sample") if f.endswith(".txt")]
for i in range(len(documentFiles)):
    documentFiles[i] = int(documentFiles[i].split(".")[0])
documentFiles.sort()
# print(documentFiles)
N = len(documentFiles)


def take_query():
    input_query=input("search here: ")
    query = set(())
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

    print(query)
    for w in query:
        print(w,dictionary.meaning(w))

    find_rank_doc(query) # function call to rank docs



def find_rank_doc(query):
    with open("./score_per_word.json") as file3:
        tf_idf = json.load(file3)

    score = {} 

    for i in range(N):
        score[i] = 0
        for word in query:
            if(word in tf_idf):
                score[i] += tf_idf[word][str(i)]

    '''
    with open("./final_doc_scores_after_query.json", 'w') as file1:
        json.dump(score, file1)    
    '''

    findtop10(score)   


def findtop10(score_final):
    #with open("./final_doc_scores_after_query.json") as data:
    #    score_list = json.load(data)
    sorted_list=sorted(score_final,key=score_final.get,reverse=True)
    #print(sorted_list)
    print("Docs ranked as follows:\n")
    for i in sorted_list[:10]:
        print(str(documentFiles[i]) + ".txt", score_final[i])



# First call to take_query() to take input from user
take_query()

    


