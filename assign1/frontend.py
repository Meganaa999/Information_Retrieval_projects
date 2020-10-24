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
	exec(query)

	# Loading metadata of the poems, to get the titles
	with open("./metadata/gutenberg-metadata.json") as file_m:
		metadata = json.load(file_m)

	with open("./final_doc_scores_after_query.json") as data:
		score_list = json.load(data)
	sorted_list=sorted(score_list,key=score_list.get,reverse=True) 
	for i in sorted_list[:10]:
		#docname = docname.split(":")
		#html+="<div class=\"row\"><div style=\"margin-left:90px\"><a class='resultxx'>"+ "Song &nbsp;:&nbsp " + i[0] + "Artist :" + docname[2] +  "</a><br></div><br>"
		html+="<div><div style=\"margin-left:90px\"><a class='resultxx'>"+ metadata[str(documentFiles[int(i)])]["title"][0] +"</a><br></div><br>"
	
	html+="<div class='text-center'><h3><a href=/>Search Again</a></h3></div>"
	html+="</body></html>"

	return html


if __name__ == '__main__':
	app.run(debug = True)