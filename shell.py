from os import system, name

def cls():system("clear" if name == "" else "cls")

class shell:
	def __init__(self):
		self.is_running = True

	def help(self):
		max = 0
		commands: list[str][str] = [i.split(" - ") for i in [
			"help - displays this message",
			"clear - clears the screen",
			"compile - starts the compiler",
			"settings - opens the settings menu",
			"exit - exits the program",
		]]
		for i in commands:
			if len(i[0]) > max: max = len(i[0])
		for i in commands: print(f"{i[0].ljust(max)} - {i[1]}")
		print()

	def run(self,command):
		match command:
			case "exit"|"esc":
				self.is_running = False
			case "clear"|"cls":
				cls()
			case "help":
				self.help()

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
				pass
