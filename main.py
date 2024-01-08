from sys import argv
from os import chdir
from script.lib.basic import cls
from script.shell import shell

cls()

def start(word):
	global param
	match word:
		case "init":
			global hasInit
			if not hasInit:
				import script.init
				script.init
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
	"localhost": None
}

hasInit = False
for i in argv[1:]: start(i)


if param['host']:
	from script.lib.localhost import startLocalhost
	param["localhost"] = startLocalhost("compiled", param["hostPort"])

try: shell(param).shell()
except KeyboardInterrupt: print()

if param["host"]:
	from script.lib.localhost import stopLocalhost
	stopLocalhost(param["localhost"])
