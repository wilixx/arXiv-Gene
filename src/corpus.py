#Author: Hamzeh Alsalhi December 2013
# Collects all necessary operations with significance on the data of a corpus of documents
from document import document
import os
from os import listdir
from os.path import isfile, join, isdir

class corpus:
	# Dictionary of document objects that this corpus contains (ID,document) pairs
	documents = {}

	# Set of unqiue english words in this corpus
	words = set([])

	def add_document(self,file_path):
		# Initializes this file as a new document in the corpus
		
		# load the data
		f = open(join(file_path), 'r')
		raw_data = f.read()
		f.close()

		# create the document object
		self.documents[file_path] = document(self,raw_data,file_path.split("/")[-1])

	def load_documents(self,corp_dir):
		# Loads all files in dir as documents
		files = [join(dp,f) for dp, dn, fn in os.walk(os.path.expanduser(corp_dir)) for f in fn]
		for f in files: 
			if not isdir(f):
				self.add_document(f)

	def __init__(self,corp_dir):
		self.load_documents(corp_dir)
		print(self.words)

	def add_words(self,word_set):
		# add word set to words
		self.words = self.words | word_set

	def get_documents_post_date(self,doc):
		# Returns the set of documents that were published after doc
		pass

	def set_citations(self):
		# sets the citaton data in every document in the corpus
		pass

	def set_influence(self):
		# sets the influence data in every document in the corpus 
		pass