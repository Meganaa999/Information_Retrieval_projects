# Information-Retrievel

### Order of executing the files.
```
$ python3 document_tokenizer.py
$ python3 term_frequency_generator.py
$ python3 tf-idf.py
$ python3 frontend.py
```
**NOTE- Once we have populated the json files after executing the first 3 commands, only frontend.py needs to be executed each time.


## Installation:

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
### Installing `PyDictionary`

```
$ pip3 install PyDictionary

```

### Installing `Flask`

```
$ pip3 install Flask

```


## Data structures used per file:

1. document_tokenizer.py
    documentFiles : List of strings which has names of all files in Corpus.
    document_tokens_list : A list of Lists of strings which stores the final tokens of corpus Document-wise.
         
2. term_frequency_generator.py
    vocabulary : Dictionary consisting of Unique words(strings) as key, and their frequency(int) in corpus as values.
    term_frequency : List of Dictionaries - having key as words, and values as term frequency per Document


3. tf-idf.py
    vocabulary_idf : Dictionary consisting of unique words from vocabulary as tokens and The document frequenices as the values
    tf_idf_per_word : Dictionary of Dictionaries -> Dictionary with key as vocabulary words 
                                                    -> Dictionary with key as Document index
                                                        -> Value as Corresponding tf-idf values.    

4. query_tokenizer.py
    i. preprocessing(query)
        queryfin : A set to store the processed unique tokens from the query

    ii. find_rank_doc(query)
        score_final : A Dictionary to store the final weighted scores of each document based on tf-idf scores of input query tokens

5. frontend.py
    i. result()
        html : A string to store the html code for the results webpage

    ii. find_dict_meaning(query_new)
        dict_meaning : A Dictionary that stores the corresponding meaning for each input query token ( Using module PyDictionary)    


## Creating The GUI
GUI has been created using flask framework of python and the front end web pages have been designed using HTML, CSS and Bootstrap.
We have also provided dictinary meanings for every term in the query using PyDictionary.

The Poem Search Engine Home Page


After running 
## Machine specs:
1. Processor: i7 4700HQ
2. Ram: 24 GB DDR3
3. OS: Ubuntu 16.04 LTS

## Results
Index building time:
- No stemming/lemmatization - 41.67s
- Stemmed text + stopwords_removal - 146.13 s

Memory usage (RAM) while building the index: around 8 GB for 3000 documents, 1.3 GB for 800 files  .
