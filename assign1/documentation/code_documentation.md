# Code Documentation
the files for which the documentation is being done are :
1. document_tokenizer.py
2. term_frequency_generator.py
3. tf-idf.py
4. query_tokenizer.py
5. frontend.py

## Modules/ libraries which were imported
- pyDictionary

## document_tokenizer.py

### create_tokens_list(): 
- Function for creating document_tokens_list and then storing in json file for further usage and then function is being called.
    - Data taken from : /corpus_sample/x.txt  where x is the file number
    - Data is 
	-Tokenized
	-Converted to lowercase
	-Stopwords are removed  
	-Stemming is done
    - Final processed data stored in : document_tokens_list.json



## term_frequency_generator.py
- to_make_vocabulary_and_term_freq() is called which in turn accesses make_vocabulary() function to build the vocabulary and make_term_freq_for_doc_i() to get frequency of term per document. 
  The descriptions of the functions are given below :

### make_vocabulary():
 	- Function for building the vocabulary i.e. the dictionary which has all the unique words in the corpus
     		- Parameters given: Document tokens which is data taken from : ./document_tokens_list.json
     		- Unique words from each document token processed in a for loop to get unique words
     		- Data stored in : ./vocabulary.json


###  make_term_freq_for_doc_i()
 	- Function for building a dictionary of frequencies for doc i
    		- Parameters given: Document tokens which is data taken from : ./document_tokens_list.json
     		- Each word in a doc mapped to its frequency in that particular document
     		- Data stored in : ./term_frequencies.json




## tf-idf.py
The code here is for calculating document frequency per word for idf calculation and finally calculating tf-idf values for every word in vocabulary.
Functions called are to_get_document_frequencies() and scorecalc().

The descriptions of the functions are given below :

### to_get_document_frequencies()
-Data accessed from : term_frequencies.json, vocabulary.json
-Function called:
	#### score_calc_per_word()
	-Calculates tf-idf values of each word for each document in the form of a dictionary of dictionaries.
	-Parameters: term_freq_list, vocabulary, doc_freq_per_word, total number of documents in corpus
-Data stored in: score_per_word.json


### storecalc()
-Data accessed from : term_frequencies.json, vocabulary.json, doc_freq_per_word.json
-Function called:
	#### docfreqperword()
	-This function gets the frequency of documents containing a vocabulary word
	-Parameters: doc_freq_list, vocabulary
-Data stored in: doc_freq_per_word.json



## query_tokenizer.py
- The code for entire query processing and calculating the results based on scores of the terms of query. Entire file is accessed from frontend.py.
All the necessary functions called by exec() function which inturn is called in frontend.py file.
Functions are as follows:

### preprocessing(query)
-  Function for inputting query and performing query based operations. It performs the following features:
    1. Applying stemming 
    2. Lemmatizing	
    3. Ommiting stopwords
    4. Changing to lowercase
    5. Tokenizing
- Returning the query

### find_rank_doc(query)
- Function will calculate the scores for every document based on query and return top 10 ranked documents
- Data accessed from : score_per_word.json
- Function called:
	#### findtop10()
	- Returns top 10 ranks
	- Parameters: score_list



## frontend.py
-This code contains is the result page which shows the Poem results based on the queries using Flask,bootstrap
-Runs a function exec from query_tokenizer.py
-Displays top 10 list of documents ranked in descending order
-Also displays meaning of words in the query


