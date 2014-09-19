# Author: Hamzeh Alsalhi December 2013
# Defines similarity functions on any two paper feature vectors
# Defines _most_similar which finds the most similar paper given a query

def _place_holder_sim(vec1,vec2):
    sim = 0.0
    return sim

def _most_similar(query,papers,sim_fun):
    # Return argmax{sim_fun(query,paper)} over papers
    pass