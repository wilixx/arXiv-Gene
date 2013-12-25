# Author: Hamzeh Alsalhi December 2013
# Processes the collection of untouched ArXiV .tex files into two data sets:
# 	1) A barebones representation for each paper.
#	2) A feature vector representation for each paper
import numpy as np
import scikit


def _to_barebones(paper):
	raise NotImplementedError
	bare = None
	return bare

def _to_feature(paper):
	raise NotImplementedError
	ftr = None
	return bare

def _get_word_prob(word):
	# Returns the probability that this word has occured in the document
	# essentially retruns theta_j for the j'th word in the document
	# p.3 shaparenko joachims 07
	raise NotImplementedError
	prob = 0.0
	return prob

def _get_prob(paper):
	# Returns the probability that this paper contains the words it contains
	# essentialy returns theta^i for the ith document
	# p.3 shaparenko joachims 07
	raise NotImplementedError
	#TODO: list fold over a the word vector and accumulate by multiplying word probabilites
	prob = 0.0
	return prob

def _knn(paper, k):
	# Returns the k nearest papers to this paper
	# options include tf vs tfidf paper reprsentation
	raise NotImplementedError
	#TODO: Call sci-kit learns's knn for now
	nbrs = {}
	return nbrs

def _cos_sim(v1,v2):
	# Returns cos sim of v1 and v2
	raise NotImplementedError
	#TODO: Call numpy's cosine similarity function for now
	sim = 0.0
	return sim

def _get_TFIDF_vector(paper):
	# Returns the the TFIDF vector representation of this paper
	# mentioned passingly on p.5 shaparenko joachims 07
	raise NotImplementedError
	tfidf = []
	return tfidf

def _get_tf_vector(paper):
	# Returns the tf vector representation of this paper
	# mentioned passingly on p.5 shaparenko joachims 07
	raise NotImplementedError
	tf = []
	return tf

def _process():
	# Processes any new papers in the untouched ArXiV .tex folder
	print("Processesing New Papers")
	raise NotImplementedError
	new_papers = []
	for paper in new_papers:
		bare = _to_barebones
		ftr = _to_feature
		# Write files: bare, ftr 

def _influential(paper, citations):
	# Reutrns a set of influential papers for the paper givien
	# -paper: the id of the paper in the database
	# -citations: boolean flag to indicate wheather or
	# not citations should be included in the retun set
	print("Finding Influential Papers ","citations" ,
		"included" if citations == 'true' else "excluded")
	raise NotImplementedError
	inf = {}
	return inf

def _get_time_stamp(paper):
	# Reutrns the timestmap in date format of when this paper was written
	raise NotImplementedError
	stamp = ""
	return stamp

def _citations(paper):
	# Returns a set of citations for a paper
	raise NotImplementedError
	cit = {}
	return cit

def _LRT(paper,candidate):
	# Detects whether candidate has significantly the paper
	# Returns a boolean flag
	raise NotImplementedError
	flag = False
	return flag