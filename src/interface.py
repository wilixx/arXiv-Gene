#Author: Hamzeh Alsalhi December 2013
# Gives an interface for making similarity queries on ArXiV.com publications
import similarity
import processor

UNTOUCHED_ARXIV_PAPERS = "path"
PROCESSED_ARXIV_PAPERS = "path"
ext = False

def _prompt_proc():
	inp = input("Process untouched ArXiV papers to look for new papers first? (y,n)")
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
				print("No paperID given for 'sim paperID'")
			pass
		else:
			print("Command is not supported.")

def _query(paper_id):
	_prompt_proc()
	results = None
	# results.print

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
