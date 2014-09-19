# Author: Hamzeh Alsalhi December 2013
# Collects all necessary operations with significance on the data of a single 
# document in the corpus
import re
from datetime import datetime, date, time
import numpy as np

class document:

	# Log file to append diagnostic output to
	log_file = None

	# File name
	file_name = None

	# Unique ID in the corpus
	ID = None

	# Publication date
	published = None

	# Document title
	title = None

	# The corpus object that this document exists in
	corpus = None

	# The raw data that represents this document
	raw = None

	# The raw data stripped down to only english words, no special
	# syntax included
	english = None

	# Numpy array of the raw data stripped down to only english words, no 
	# special syntax included
	np_english = None

	# Set of all english words in this documents
	words = None

	def get_english(self,raw):
		# return the english word list representation of raw
		return [w for w in raw.split() if re.match('^[a-zA-Z0-9\']+$',w) 
				is not None]

	def parse_ID(self,s):
		# Parses the line that contains the ID for a clean ID
		return s.split()[0]

	def parse_date(self,s):
		# Parses the string that represents the date into a date object
		year_str = str(s[:2])
		month_str = str(s[2:4])
		date = datetime.strptime("01"+month_str+year_str,"%d%m%y")
		return date

	def load_meta_information(self,raw):
		# Loads ID and publication date

		# Loads ID
		ID_str = re.search('%Paper:(.*)\n',raw[:500])
		if(not ID_str == None):
			self.ID = self.parse_ID(ID_str.group(1))
			# Loads publication date
			self.published = self.parse_date(self.ID.split("/")[-1][:4])
		else:
			self.ID = "NA"
			self.log_file.write("ID not found for paper " + self.file_name + 
								"\n")

	def __init__(self,corp,raw_data,file_name):
		from interface import log_file_path
		self.log_file = open(log_file_path,'a')

		self.corpus = corp

		# process into three bare representaions
		self.raw = raw_data
		self.english = self.get_english(self.raw)
		self.np_english = np.array(self.english)
		self.words = set(self.english)

		# Fill in meta information
		self.file_name = file_name
		self.load_meta_information(self.raw)

		# update the corpus word set
		self.corpus.add_words(self.words)

		self.log_file.close()


	# The term frequency vector for this paper in realtion to its corpus as np
	# array
	TF = None

	# The TFIDF vector for this paper in realtion to its corpus as np array
	TFIDF = None

	# The estimator as defined in shaparenko 07 to be TF/len(english) for this
	# document as np array
	estimator = None

	# List of documents in the corpus that this document cites
	citations = None

	# List of documents in the corpus that site this one in the corpus
	cited_by = None

	# List of documents in the corpus that influence this one
	influences = None

	# List of documents in the corpus that this document has influenced
	influenced = None

	def construct_TF_vector(self, corpus_word_list, np_eng):
		# Constructs a vector of length len(corpus_word_list) that counts 
		# how many times each word in english occurs
		tf = np.array([0] * len(corpus_word_list))
		for i in range(len(corpus_word_list)):
			tf[i] = len(np.where(np_eng == corpus_word_list[i])[0])
		return tf

	def construct_estimator(self, corpus_word_list, np_eng):
		# Constructs a vector of length len(corpus_word_list) that counts how
		# many times each word in english occurs and divides each element by
		# len(np_eng)
		tf = np.array([0] * len(corpus_word_list))
		for i in range(len(corpus_word_list)):
			tf[i] = len(np.where(np_eng == corpus_word_list[i])[0])
		return tf/float(len(np_eng))

	def construct_relational_fields(self):
		# Build the fields of a document that depend on having a completly 
		# defined corpus such as TF, TFIDF, cited_by, and more
		self.TF = self.construct_TF_vector(self.corpus.words,self.np_english)
		self.estimator = self.construct_estimator(self.corpus.words,
												  self.np_english)
