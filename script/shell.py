from os import getcwd, listdir, path, remove, system, name as osName
from script.lib.basic import alignText, readVersion
from script.lib.zip import zip_file
from script.settings import settings
from script.compiler import compiler

def cls():system("clear" if osName == "" else "cls")

class shell:
	def __init__(self,param):
		self.is_running = True
		self.settings = settings(param)
		self.compiler = compiler(self.settings)

	def help(self):
		print(alignText([
			"help - displays this message",
			"clear - clears the screen",
			"compile - starts the compiler",
			"settings - opens the settings menu",
			"clearCache - Empty the whole cache"
			"exit - exits the program",
		], " - "))

	def run(self,command: str):
		match command.strip().lower():
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
			case _:
				print(f"Unknown command '{command}'")

	def shell(self):
		cls()
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
