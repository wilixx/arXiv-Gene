# Author: Hamzeh Alsalhi December 2013
# Gives an interface for making similarity queries on ArXiV.com publications
import similarity
import processor

UNTOUCHED_ARXIV_PAPERS = "path"
PROCESSED_ARXIV_PAPERS = "path"
ext = False

def _prompt_proc():
    inp = input("Process untouched ArXiV papers to look for new papers? (y,n)")
    _command(inp,processor._process)

# Input: the raw user input as a string
# State: a argumentless function to be run if the user input is 'yes'
def _command(inp, state):
    # Interpret the first word as a command
    global ext
    inp = inp.lower()
    tkns = inp.split()
    if(len(tkns) >= 1):
        tkn = inp.split()[0];
        if tkn in ("exit", "close"):
            ext = True 
        elif tkn in ("yes","y"):
            state()
        elif tkn == "sim":
            if(len(tkns) >= 2):
                _query(tkns[1])
            else:
                print("No paper ID given for command 'sim ID'")
            pass
        elif tkn == "inf":
            if(len(tkns) >= 3):
                processor._influential(tkns[1],tkns[2])
            else:
                print("No ID given command 'inf ID include_citation_flag'")
        else:
            print("Command is not supported.")

# Cecks if the user givin query is a valid id for any paper in the collection
def _valid_id(paper_id):
    return True

def _query(paper_id):
    if _valid_id(paper_id):
        _prompt_proc()
        results = None
        # results.print
    else:
        print("Invalid paper ID")

def _listen():
    global ext
    if not ext:
        inp = input("Enter a Command, 'exit' to exit:")
        _command(inp,None)
        _listen()

if __name__ == "__main__":
    import sys
    if len(sys.argv) >=  2:
        _command(sys.argv[1])
    _listen()
