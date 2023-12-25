from sys import argv
from os import chdir
from script.shell import shell

def init():
	"""
	create all the necessary files and folders
	"""
	from json import dump
	from os import mkdir, listdir
	# create the htmlCompilerSettings.json file
	settings = {
		"htmlCompilerVersion": 1,
		"autoCompile": True,
		"compileDelay": 10, # seconds
		# add settings here
	}
	# create the htmlCompilerCache.json file
	with open("htmlCompilerCache.json", "w") as f: f.write("{}")
	with open("htmlCompilerSettings.json", "w") as f:
		dump(settings, f, indent="\t")
	# create the run and compiled folder
	if not "run" in listdir():mkdir("run")
	if not "compiled" in listdir():mkdir("compiled")
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
