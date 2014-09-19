arXiv-Gene
=========

Describes the relations between academic papers on ArXiv.com as written in this paper http://www.benyah.net/publications/InformationGenealogy_KDD07.pdf.

This method gives a way to find relations between documents in a corpus which are shown to generate better similarity data than the naive feature vector distance measures.


The goal of this project is first to develop the necessary infrastructure to recreate the results on the data sets used in the paper and then afterward expand the code base to make it easy to run similar experiments on corpuses of different format and content.

The entry point for running the code is interface.py

# Components
- [x] Load local arXiv corpus and calculate tf vectors
- [ ] fast knn from scikit-learn
- [ ] convex optimization function ontop of mosek
- [ ] Relational graph construction
