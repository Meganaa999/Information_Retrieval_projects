import sys
import glob
import os
from math import log
import nltk
from nltk import word_tokenize

import sys
import math
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
import pickle
import json
import query_tokenizer
from query_tokenizer import exec

from PyDictionary import PyDictionary
dictionary=PyDictionary()

from flask import Flask, redirect, url_for, request, render_template

documentFiles = [f for f in os.listdir("./corpus_sample") if f.endswith(".txt")]
for i in range(len(documentFiles)):
    documentFiles[i] = int(documentFiles[i].split(".")[0])
documentFiles.sort()

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")
'''
this is the result page which shows the Poem results based on the queries 
'''
@app.route('/result',methods = ['POST', 'GET'])
def result():
	
	
	if request.method == 'POST':
		query = request.form["query"]
	print(query)
	html="<!DOCTYPE html> <head><link rel=stylesheet type=text/css href=static/styles/bootstrap.min.css> <link rel=stylesheet type=text/css href=static/styles/style.css></head><body>"
	html+="<div class='text-center'><h2>Search results for <i><b>"+query+"</b></i></h2></div><hr>"

	#print("Hello" + query)
	query_new, score_list = exec(query)
	
	mean = find_dict_meaning(query_new)
	# Loading metadata of the poems, to get the titles
	with open("./metadata/gutenberg-metadata.json") as file_m:
		metadata = json.load(file_m)
	
	sorted_list=sorted(score_list,key=score_list.get,reverse=True) 
	for w in mean:
		html+="<div class='dict'>" + str(mean[w])+"</div>"
	for i in sorted_list[:10]:
		file_link= r'http://www.gutenberg.org/ebooks/' 
		file_link+=str(documentFiles[int(i)])
		#x=str(documentFiles[int(i)])
		html+="<div><div style=\"margin-left:90px\"><a class='resultxx' href="+file_link+" }>"+ metadata[str(documentFiles[int(i)])]["title"][0] +"</a><br></div><br>"
		#html+="<b href="file_link">file_link</b>"
	
	html+="<div class='text-center'><h3><a href=/>Search Again</a></h3></div>"
	html+="</body></html>"

	return html


def find_dict_meaning(query_new):
	dict_meaning={}
	for w in query_new:
		dict_meaning[w] = dictionary.meaning(w)
	return dict_meaning

if __name__ == '__main__':
	app.run(debug = True)