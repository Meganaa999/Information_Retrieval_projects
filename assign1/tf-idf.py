import json
import os
import math
vocabulary_idf = {}


def docfreqperword(doc_freq_list, vocabulary):

    z = 0
    for word in vocabulary:
        z += 1
        # print(z)
        for doc in doc_freq_list:
            if word in doc:
                if word in vocabulary_idf:
                    vocabulary_idf[word] = vocabulary_idf[word] + 1
                else:
                    vocabulary_idf[word] = 1


tf_idf_per_word = {}


def score_calc_per_word(doc_freq_list, vocabulary, doc_freq_per_word, N):

    # z=0
    for word in vocabulary:
        # z+=1
        # print(z)
        #score = 0
        docno = 0
        score = []
        for doc in doc_freq_list:
            if word in doc:
                score.insert(docno, doc[word] *
                             (math.log2(N/doc_freq_per_word[word])))
            else:
                score.insert(docno, 0)
            docno = docno+1

        # print(score)
        tf_idf_per_word[word] = score


def scorecalc():
    with open("./term_frequencies.json") as data:
        term_freq_list = json.load(data)
    with open("./vocabulary.json") as data:
        vocabulary = json.load(data)
    with open("./doc_freq_per_word.json") as data:
        doc_freq_per_word = json.load(data)
    documentFiles = [f for f in os.listdir(
        "./corpus_sample") if f.endswith(".txt")]
    N = len(documentFiles)
    score_calc_per_word(term_freq_list, vocabulary, doc_freq_per_word, N)
    print("scores loaded")
    # Dumping the created vocabulary into a json for further use
    with open("./score_per_word.json", 'w') as file2:
        json.dump(tf_idf_per_word, file2)


def to_get_document_frequencies():
    with open("./term_frequencies.json") as data:
        term_freq_list = json.load(data)
    with open("./vocabulary.json") as data:
        vocabulary = json.load(data)

    docfreqperword(term_freq_list, vocabulary)
    print("frequencies loaded")

    # Dumping the created vocabulary into a json for further use
    with open("./doc_freq_per_word.json", 'w') as file1:
        json.dump(vocabulary_idf, file1)


to_get_document_frequencies()
scorecalc()
