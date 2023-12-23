from json import load, dump
from lib import align, sec2hours

class settings:
	def __init__(self):
		with open("htmlCompilerSettings.json", "r") as f:
			loaded = load(f)

		self.version = loaded["htmlCompilerVersion"]
		self.autoCompile = loaded["autoCompile"]
		self.compileDelay = loaded["compileDelay"]
		# add settings here
	def save(self):
		with open("htmlCompilerSettings.json", "w") as f:
			dump({
				"htmlCompilerVersion": self.version,
				"autoCompile": self.autoCompile,
				"compileDelay": self.compileDelay,
				# add settings here
			}, f, indent="\t")
	def help(self):
		print()
		print(align([
			"autocompile - toggles whether the compiler will automatically compile files when they are saved",
			"compiledelay - sets the delay between each time the compiler will check for files to compile (in seconds)",
			# add settings here
		], " - "))
		print("""
Type 'exit' to return to the main menu
Type 'reset' to reset all settings to default
""")
	def menu(self):
		print("Settings Menu")
		while True:
			command = input("\r\033[91mHtmlCompiler Settings\033[0m >>> ").split(" ")
			match command[0].lower():
				case "exit"|"esc": return
				case "help": self.help()
				case "": pass
				case "reset":
					self.autoCompile = True
					self.compileDelay = 600
					# add settings here
					print("Settings have been reset to default")
					self.save()
				case "autocompile":
					if len(command) == 1:
						print(f"Autocompile is currently set to {self.autoCompile}")
					elif command[1].lower() == "true": 
						self.autoCompile = True
						print("Autocompile has been set to True")
						self.save()
					elif command[1].lower() == "false":
						self.autoCompile = False
						print("Autocompile has been set to False")
						self.save()
				case "compiledelay":
					if len(command) == 1:
						print(f"Compile delay is currently set to {sec2hours(self.compileDelay)}")
					elif command[1].isdigit():
						self.compileDelay = int(command[1])
						print(f"Compile delay has been set to {sec2hours(self.compileDelay)}")
						self.save()
					else:
						print("Invalid compile delay")
						print("Compile delay must be a number")
				# add settings here
				case _: print(f"Unknown command '{command[0]}'")
