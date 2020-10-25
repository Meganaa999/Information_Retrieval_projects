# Design Document for Creating a domain specific information retrieval system
The application created by the group is a domain specific search engine 
The domain we have selected is Poetry.

## Team Members
- RUPSA DHAR (2018A7PS0376H)
- KESHAV KABRA (2018AAPS0527H)
- MEGANAA REDDY (2017B3A7PS0376H)


## The program/application can be broken down into the various subparts :
1. document_tokenizer.py: 
Stores the tokenized words of each document as lists and then the corresponding list is stored in a json file.

2. term_frequency_generator.py: 
Stores all the unique words present in the corpus along with frequencies in each document

3. tf-idf.py
Creates a dictionary which contains the words in the vocabulary as the key and the value as another dictionary which contains each document as key and its value contains the TF-IDF values.

4. query_tokenizer.py: 
Takes query as input and calculates the scores for each document.

5. frontend.py: Contains the gui program writtem in flask framework for python to accept query and receive the names of the top 10 documents with the highest scores

### Order of executing the files.
```
$ python3 document_tokenizer.py
$ python3 term_frequency_generator.py
$ python3 tf-idf.py
$ python3 frontend.py
```
**NOTE- Once we have populated the json files after executing the first 3 commands, only frontend.py needs to be executed each time.


## Installation:

Run the follwing in terminal.
```
$ pip install -r requirements.txt

```
If you face any problem, install `nltk` separately.

### Installing `nltk`

```
$ pip3 install nltk
$ python3
>>> import nltk
>>> nltk.download()
	Packages: all
```


## Data structures used per file:

### document_tokenizer.py
    documentFiles : List of strings which has names of all files in Corpus.
    document_tokens_list : A list of Lists of strings which stores the final tokens of corpus Document-wise.
         
### term_frequency_generator.py
    vocabulary : Dictionary consisting of Unique words(strings) as key, and their frequency(int) in corpus as values.
    term_frequency : List of Dictionaries - having key as words, and values as term frequency per Document


### tf-idf.py
    vocabulary_idf : Dictionary consisting of unique words from vocabulary as tokens and The document frequenices as the values
    tf_idf_per_word : Dictionary of Dictionaries -> Dictionary with key as vocabulary words 
                                                    -> Dictionary with key as Document index
                                                        -> Value as Corresponding tf-idf values.    

### query_tokenizer.py
    i. preprocessing(query)
        queryfin : A set to store the processed unique tokens from the query

    ii. find_rank_doc(query)
        score_final : A Dictionary to store the final weighted scores of each document based on tf-idf scores of input query tokens

### frontend.py
    i. result()
        html : A string to store the html code for the results webpage

    ii. find_dict_meaning(query_new)
        dict_meaning : A Dictionary that stores the corresponding meaning for each input query token ( Using module PyDictionary)    


## Creating The GUI
GUI has been created using flask framework of python and the front end web pages have been designed using HTML, CSS and Bootstrap.
We have also provided dictinary meanings for every term in the query using PyDictionary.

After running 
## Machine specs:
1. Processor: i5-8250U
2. Ram: 8 GB DDR3
3. OS: Windows 10 WSL2 kernel

## Results
- Preprocessing time (Tokenizing, Normalization, Stemming) : 581.4531 s

- Index Building time : 29.7234 s


Memory usage (RAM) while building the index: around 300 MB for 200 huge poem documents   .