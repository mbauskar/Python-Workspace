#redirect.py
#Python Program to redirect the stdout object so it will print the result in 'output' file instead of terminal

import sys

class StdoutRedirect:
	def __init__(self, newOut):	# executed after instance of class is created 
		self.newOut = newOut

	def __enter__(self):		# executed after __init__ , Python calls it when entering the context i.e. at the beginning of with statement
		self.oldOut = sys.stdout
		sys.stdout = self.newOut

	def __exit__(self, *args):	# called after exiting the context i.e end of with statement
		sys.stdout = self.oldOut

print 'X'
with open('output', 'w') as myfile:
	with StdoutRedirect(myfile):
		print 'redirecting stdout to "output" file instate of terminal'

print 'Z'
