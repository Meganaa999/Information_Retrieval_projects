import nltk
# nltk.download("stopwords")
from nltk.stem.snowball import SnowballStemmer
import os
import json

document_tokens_list = []
stemmer = SnowballStemmer('english')

# List of all documents 
documentFiles = [f for f in os.listdir("./corpus_sample") if f.endswith(".txt")]

# Storing only the name of txt file
for i in range(len(documentFiles)):
    documentFiles[i] = int(documentFiles[i].split(".")[0])
    
documentFiles.sort()
print(documentFiles)


def create_tokens_list():
    '''
    Creates a list of token of each documents separately and appends them to a a json file. 
    '''

    cnt = 0 # Counter to keep count of files.
    for item in documentFiles:
        file_name = open("./corpus_sample/" + str(item) + ".txt")
        print("Working on " + str(item) + ".txt")
        text = file_name.read()
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        temp_tokens = tokenizer.tokenize(text) # Word Tokenizing
        # temp_tokens = nltk.word_tokenize(text) 
        temp_tokens = [token.lower() for token in temp_tokens if token.isalnum()] # Converting to lower case and removing punctuation
        temp_tokens = [ token for token in temp_tokens if token not in nltk.corpus.stopwords.words('english')] # Removing stop words
        temp_tokens = [stemmer.stem(token) for token in temp_tokens] # Stemming
        document_tokens_list.append(temp_tokens)
        cnt += 1
    
    print(str(cnt) + " Files tokenized.")


    # Storing in json for better accessibility
    with open("./document_tokens_list.json",'w') as f1:
        json.dump(document_tokens_list,f1)



create_tokens_list()

