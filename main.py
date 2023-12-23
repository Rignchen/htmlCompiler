from sys import argv
from os import chdir
from shell import shell

def init():
	## create all the necessary files and folders
	# create the htmlCompilerSettings.json file
	from json import dump
	settings = {
		"autoCompile": True,
		"compileDelay": 600, # = 10 minutes
		# add settings here
	}
	with open("htmlCompilerSettings.json", "w") as f:
		dump(settings, f, indent="\t")
	# create the run and compiled folder
	from os import mkdir
	mkdir("run")
	mkdir("compiled")
	# create the gitignore file
	with open(".gitignore", "w") as f:
		f.write("compiled\nhtmlCompilerSettings.json")
def start(word):
	match word:
		case "init":
			init()
			print("Initialized!")
		case _:
			chdir(word)

for i in argv[1:]: start(i)

shell().shell()
