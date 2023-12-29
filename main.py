from sys import argv
from os import chdir
from script.lib.basic import cls
from script.shell import shell

cls()

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
		f.write("""
compiled/
htmlCompilerCache.json
htmlCompilerModelsCache.json
htmlCompilerSettings.json
null
""".replace("\n", "", 1))
	system("git init")
def start(word):
	global param
	match word:
		case "init":
			global hasInit
			if not hasInit:
				init()
				hasInit = True
				print("Initialized!")
		case "compilerDebug":
			param["compilerDebug"] = not param["compilerDebug"]
		case "host"|"localhost":
			param['host'] = not param['host']
		case _:
			arg = word.split("-",1)
			match arg[0]:
				case "host"|"localhost":
					param['host'] = True
					param["hostPort"] = int(arg[1])
				case _:
					chdir(word)

param = {
	"compilerDebug": False,
	"host": False,
	"hostPort": 8080,
}

hasInit = False
for i in argv[1:]: start(i)


if param['host']:
	from script.lib.localhost import startLocalhost, stopLocalhost
	thread = startLocalhost("compiled", param["hostPort"])
	print(thread[1].recv())

try: shell(param).shell()
except KeyboardInterrupt: pass

finally:
	if param["host"]:
		stopLocalhost(thread)
