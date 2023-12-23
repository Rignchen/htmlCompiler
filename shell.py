from os import system, name

def cls():system("clear" if name == "" else "cls")

is_running = True

def run(command):
	match command:
		case "exit"|"esc":
			global is_running 
			is_running = False
		case "cls":
			cls()

def shell():
	global is_running
	cls()
	print("Welcome to HtmlCompiler!")
	while is_running:
		try:
			# ask the user for input by saying "HtmlCompiler" in green, follow by " >>>" in white
			command = input("\033[92mHtmlCompiler\033[0m >>> ")
			run(command)
		except KeyboardInterrupt:
			pass
