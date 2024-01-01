from os import getcwd, listdir, path, remove
from script.lib.basic import alignText, cls, readVersion
from script.lib.localhost import startLocalhost, stopLocalhost
from script.lib.zip import zip_file
from script.settings import settings
from script.compiler import compiler

class shell:
	def __init__(self,param):
		self.is_running = True
		self.settings = settings(param)
		self.compiler = compiler(self.settings)

	def help(self):
		helpMessage = [
			"help - displays this message",
			"clear - clears the screen",
			"compile - starts the compiler",
			"settings - opens the settings menu",
			"clearCache - Empty the whole cache",
			"host - Stop the localhost, you can add \"force\" to kill it" if self.settings.param["host"] 
			else "host - Start a localhost, you can specify the wanted port",
			"exit - exits the program",
		]
		print(alignText(helpMessage, " - "))

	def run(self,command: str):
		commands = command.lower().split(" ")
		match commands[0].strip():
			case "":
				pass
			case "exit"|"esc":
				self.is_running = False
			case "clear"|"cls":
				cls()
			case "help":
				self.help()
			case "settings"|"set":
				self.settings.menu()
			case "compile"|"build"|"start":
				self.compiler.start()
			case "clearcache":
				self.compiler.cache = {}
				self.compiler.saveCache()
				self.compiler.models = {}
				self.compiler.saveModels()
			case "zip":
				name = path.basename(getcwd()) + ".zip"
				if name in listdir(): remove(name)
				zip_file(["compiled"], name)
			case "host":
				if self.settings.param["host"]:
					if "force" in commands:
						self.settings.param["localhost"][0].kill()
					else:
						stopLocalhost(self.settings.param["localhost"])
					self.settings.param["host"] = False
				else:
					if 1 < len(commands) and commands[1].isdigit() and len(command[1]) <= 4:
						self.settings.param["hostPort"] = int(commands[1])
					self.settings.param["localhost"] = startLocalhost("compiled", self.settings.param["hostPort"])
					self.settings.param["host"] = True
					print(self.settings.param["localhost"][1].recv())
			case _:
				print(f"Unknown command '{commands[0]}'")

	def shell(self):
		print("Welcome to HtmlCompiler!")
		print("Version:", readVersion(self.settings.version))
		print("Type 'help' for a list of commands\n")
		while self.is_running:
			try:
				# ask the user for input by saying "HtmlCompiler" in green, follow by " >>>" in white
				command = input("\r\033[92mHtmlCompiler\033[0m >>> ")
			except KeyboardInterrupt:
				self.is_running = False
			else:
				try:
					self.run(command)
				except KeyboardInterrupt:
					print()
