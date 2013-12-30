#Author: Hamzeh Alsalhi December 2013
# Collects all necessary operations with significance on the data of a single document in the corpus
import re

class document:

	# Unique ID in the corpus
	ID = None

	# The corpus object that this document exists in
	corpus = None

	# The raw data that represents this document
	raw = None

	# The raw data stripped down to only english words, no special syntax included
	english = None

	# Set of all english words in this documents
	words = None

	def get_english(self,raw):
		# return the english word list representation of raw
		return [w for w in raw.split() if re.match('^[a-zA-Z0-9\']+$',w) is not None]

	def __init__(self,corp,raw_data,file_name):
		self.corpus = corp

		# process into three bare representaions
		self.raw = raw_data
		self.english = self.get_english(self.raw)
		self.words = set(self.english)

		# update the corpus word set
		self.corpus.add_words(self.words)

		print(file_name)
		print(len(self.words))

	# The term frequency vector for this paper in realtion to its corpus
	TF = None

	# The TFIDF vector for this paper in realtion to its corpus
	TFIDF = None

	# Publication date
	date = None

	title = None

	# List of documents in the corpus that this document cites
	citations = None

	# List of documents in the corpus that site this one in the corpus
	cited_by = None

	# List of documents in the corpus that influence this one
	influences = None

	# List of documents in the corpus that this document has influenced
	influenced = None