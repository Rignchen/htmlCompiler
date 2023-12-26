from sys import argv
from os import chdir
from script.shell import shell

def init():
	"""
	create all the necessary files and folders
	"""
	from json import dump
	from os import mkdir, listdir, system
	# create the htmlCompilerSettings.json file
	settings = {
		"autoCompile": True,
		"compileDelay": 10, # seconds
		# add settings here
	}
	# create the htmlCompilerCache.json file
	with open("htmlCompilerCache.json", "w") as f: f.write("{}")
	with open("htmlCompilerModelsCache.json", "w") as f: f.write("{}")
	with open("htmlCompilerSettings.json", "w") as f:
		dump(settings, f, indent="\t")
	# create the run and compiled folder
	if not "run" in listdir():mkdir("run")
	if not "compiled" in listdir():mkdir("compiled")
	# create the gitignore file and git repo
	with open(".gitignore", "w") as f:
		f.write("compiled\nhtmlCompiler*.json\n")
	system("git init")
def start(word):
	global param
	match word:
		case "init":
			init()
			print("Initialized!")
		case "compilerDebug":
			param["compilerDebug"] = True
		case _:
			chdir(word)

param = {
	"compilerDebug": False
}

for i in argv[1:]: start(i)

shell(param).shell()
