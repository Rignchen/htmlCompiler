from os import system, name
from lib import align
from settings import settings

def cls():system("clear" if name == "" else "cls")

class shell:
	def __init__(self):
		self.is_running = True

	def help(self):
		print(align([
			"help - displays this message",
			"clear - clears the screen",
			"compile - starts the compiler",
			"settings - opens the settings menu",
			"exit - exits the program",
		], " - "))
		print("\nPressing ctrl + c will allways bring you back to the main menu\n")

	def run(self,command):
		match command:
			case "exit"|"esc":
				self.is_running = False
			case "clear"|"cls":
				cls()
			case "help":
				self.help()
			case "settings"|"set":
				settings().menu()
			case "":
				pass
			case _:
				print(f"Unknown command '{command}'")

	def shell(self):
		cls()
		print("Welcome to HtmlCompiler!")
		print("Type 'help' for a list of commands\n")
		while self.is_running:
			try:
				# ask the user for input by saying "HtmlCompiler" in green, follow by " >>>" in white
				command = input("\r\033[92mHtmlCompiler\033[0m >>> ")
				self.run(command)
			except KeyboardInterrupt:
				print()
