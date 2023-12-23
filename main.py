from sys import argv
from os import chdir
from shell import shell

if len(argv) > 1:
	chdir(argv[1])

shell()
