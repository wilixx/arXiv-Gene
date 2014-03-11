ArXiV_Gen
=========

Describes the relations between academic papers on ArXiv.com as written in this paper http://www.benyah.net/publications/InformationGenealogy_KDD07.pdf.

This method gives a way to find relations between documents in a corpus which are shown to generate better similarity data than the naive feature vector distance measures.


The goal of this project is first to develop the necessary infrastructure to recreate the results on the data sets used in the paper and then afterward expand the code base to make it easy to run similar experiments on corpuses of different format and content.

The entry point for running the code is interface.py


Version 0.1 - Complete
  Basic loading of the ArXiV data set as a corpus with implemented loading of document metadata and initial computation of document feature vectors and language models.
  
Version 0.2 - WIP
  The convex optimization outlined in the paper is to be solve using the separable optimization python API for Mosek.
  
