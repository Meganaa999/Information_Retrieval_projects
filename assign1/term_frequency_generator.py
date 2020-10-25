import json
import math
vocabulary = {}
def make_vocabulary(document_tokens):
    '''
    To make a vocabulary dictionary, consisting of all unique words in corpus
    '''

    for word in document_tokens:
        count = vocabulary.get(word,0)
        vocabulary[word] = count + 1


term_frequency = [] # A list of dictionaries to store term freq for each document

def make_term_freq_for_doc_i(document_tokens):
    term_freq_dict = {} # A dictionary of frequencies for doc i
    for word in document_tokens:
        count = term_freq_dict.get(word,0)
        term_freq_dict[word] = count + 1

    # Logarithmically scaling
    for term in term_freq_dict:
        if(term_freq_dict[term]>0):
            term_freq_dict[term] = math.log2(1 + term_freq_dict[term])
    return term_freq_dict


def to_make_vocabulary_and_term_freq():
    with open("./document_tokens_list.json") as data:
        document_tokens_list = json.load(data)

    i=0
    for document_tokens in document_tokens_list:
        print("Working on doc "+ str(i))
        make_vocabulary(document_tokens)
        temp_dict =  make_term_freq_for_doc_i(document_tokens)
        term_frequency.append(temp_dict)
        i+=1

    # Dumping the created vocabulary into a json for further use
    with open("./vocabulary.json", 'w') as file1:
        json.dump(vocabulary, file1) 

    with open("./term_frequencies.json", 'w') as file2:
        json.dump(term_frequency, file2) 

    print("\n Picked vocabulary and freq from "+ str(i) + " files.")


to_make_vocabulary_and_term_freq()