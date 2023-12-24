from os import system, name
from lib import align, readVersion
from settings import settings

def cls():system("clear" if name == "" else "cls")

class shell:
	def __init__(self):
		self.is_running = True
		self.settings = settings()

	def help(self):
		print(align([
			"help - displays this message",
			"clear - clears the screen",
			"compile - starts the compiler",
			"settings - opens the settings menu",
			"exit - exits the program",
		], " - "))

	def run(self,command):
		match command:
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
			case _:
				print(f"Unknown command '{command}'")

	def shell(self):
		cls()
		print("Welcome to HtmlCompiler!")
		print("Version:", readVersion(self.settings.get['htmlCompilerVersion']))
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
