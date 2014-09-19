# Author: Hamzeh Alsalhi December 2013
# Collects all necessary operations with significance on the data of a corpus of documents
from document import document
import os
from os import listdir
from os.path import isfile, join, isdir
import scipy as sp

class corpus:

    # Flag to allow "Neuron" and "neuron" to be distinguished as separate words
    allow_case_sensetivity = True

    # Flag to allow words that cannot be identified in a webbased dictionary
    allow_non_dictionary_words = True

    # Log file to append diagnostic output to
    log_file = None

    # Dictionary of document objects in this corpus (ID,document) pairs
    documents = {}

    # List of documents sorted by date
    documents_sorted = []

    # Set of unqiue english words in this corpus
    word_set = set([])

    # List of unqiue english words in this corpus
    words = []


    def add_document(self,file_path):
        # Initializes this file as a new document in the corpus
        
        try:
            # load the data
            f = open(join(file_path), 'r')
            raw_data = f.read()
            f.close()

            # create the document object
            d = document(self,raw_data,file_path.split("/")[-1])
            self.documents[d.ID] = d
        except (UnicodeDecodeError):
            self.log_file.write("UnicodeDecodeError on file " + file_path + 
                                "\n")

    def load_documents(self,corp_dir):
        # Loads all files in dir as documents
        files = [join(dp,f) for dp, dn, fn in 
                 os.walk(os.path.expanduser(corp_dir)) for f in fn]
        for f in files: 
            if not isdir(f):
                self.add_document(f)

    def __init__(self,corp_dir):
        from interface import log_file_path
        self.log_file = open(log_file_path,'a')

        #Load all documents
        self.load_documents(corp_dir)

        # Sort documents by date
        self.documents_sorted = list(self.documents.items())
        self.documents_sorted.sort(key=lambda x: x[1].published)

        # Make a word list for this corpus
        self.words = sorted(list(self.word_set))

        # Construct document relational attributes
        for d in self.documents.values():
            d.construct_relational_fields()
            self.log_file.write(str(d.TF) + d.ID + "\n")
            self.log_file.write(str(d.estimator) + "\n")

        self.log_file.write(str(self.words) + "\n")

        self.log_file.close()

    def add_words(self,w_set):
        # add word set to words
        self.word_set = self.word_set | w_set

    def set_citations(self):
        # sets the citaton data in every document in the corpus
        pass

    def set_influence(self):
        # sets the influence data in every document in the corpus 
        pass

    def get_documents_pre_date(self,new_ID):
        # Returns the set of documents that were published before new
        new = self.documents[new_ID]
        if new in self.documents_sorted:
            return set([d.ID for d in 
                        self.documents_sorted[:self.documents_sorted.index(new)]])
        else:
            return set([])

    def get_k_nearest_docuemnts(self,k,sim_func,new_ID, document_ID_set):
        # Finds the k nearest neigbors of the document new within document_set 
        # using sim_func as the simiality measure
        sims = [] 
        for d_ID in document_set: 
            sims.append( (sim_func(self.documents[new_ID].TF,
                                   self.documents[d_ID].TF),d_ID) )
        sims.sort(key = lambda x: x[0])
        nbr_IDs = []
        for i in range(k):
            if(k > len(sims)):
                break
            nbr_IDs.append(sims[k][1])
        return nbr_IDs

    def find_influences(self,new_ID):
        # Finds all influences of the document new from within this corpus
        influences = set([])
        docs_predate_IDs = get_documents_pre_date(new_ID)
        candidate_IDs = get_k_nearest_docuemnts(100, 
                                                sp.spatial.distance.cosine,
                                                docs_predate_IDs)
        for c_id in candidate_IDs:
            if influence_test(c_id,new_ID):
                influences.add(documents[c_id].ID)
        return influences

    def influence_test(self,candidate_ID, new_ID):
        # Tests if candidate is an influence on the document new
        result = False
        pass
