## Poem Search Engine

-A tf-idf based Search Engine for searching poems using query words. The main purpose of this project is understand how vector space based retrieval models work and how that can be utilised to get documents according to relevance.
 -More on [Tf-Idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf). 

## The program/application can be broken down into the various subparts (actual file names also added) :
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
$ sudo pip install -r requirements.txt
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


## DATA STRUCTURES USED:


### document_tokenizer.py
    documentFiles : List of strings which has names of all files in Corpus.
    ex: If the corpus contains 2 documents:
    	documentFiles[]=["abc.txt","shakespeare.txt"]
    document_tokens_list : A list of Lists of strings which stores the final tokens of corpus after tokenizing,stemming and normalization on each token Document-wise.
    ex: If corpus conatins 2 files  abc.txt and shakespeare.txt:
    	abc.txt="Ramu is jumping on the bed"
		shakespeare.txt="Mornings are beautiful"
		document_tokens_list=[["ramu","jump","bed"],["morning","beauti"]]
         
### term_frequency_generator.py
    vocabulary : Dictionary consisting of Unique words(strings) as key, and their frequency(int) in corpus as values.
    ex:If the vocabulary contains 2 words 'play' and 'sunset':
    	vocabulary={"play":23,"sunset":3}
    term_frequency : List of Dictionaries - having key as words, and values as term frequency per Document
    ex:term_frequency=[{"play":10,"sunset":1},{"play":13,"sunset":2}]


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

### The Poem Search Engine Home page.

![](images/homepage.jpg)

### The Poem Search Engine Results page.

![](images/results.PNG)


## Machine specs:
1. Processor: i5-8250U
2. Ram: 8 GB DDR3
3. OS: Windows 10 WSL2 kernel

## Results
- Preprocessing time (Tokenizing, Normalization, Stemming) : 581.4531 s

- Index Building time : 29.7234 s


Memory usage (RAM) while building the index: around 300 MB for 200 huge poem documents   .


## Members
[Rupsa Dhar](https://github.com/rupsadhar)

[Keshav Kabra](https://github.com/everlearner)

[Meganaa Reddy](https://github.com/Meganaa999)
