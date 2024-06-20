import sys
import os

if getattr(sys, 'frozen', False):
	absPath = os.path.dirname(os.path.abspath(sys.executable))
	print('frozen')
elif __file__:
	absPath = os.path.dirname(os.path.abspath(__file__))
	print('db __file__')

print('db->', absPath)
