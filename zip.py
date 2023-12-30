from genericpath import isdir
from os import getcwd, listdir, path as osPath, remove, walk
from zipfile import ZipFile, ZIP_DEFLATED
from sys import argv

def showVersion(version: int) -> str:
	"""
	display the version number in a readable format: mm.ss.ff
	"""
	main = version // 10000
	sub = (version - main * 10000) // 100
	fix = version - main * 10000 - sub * 100
	return f"{main}.{sub}.{fix}"
def changeVersion(start: int, end: int, version: int):
	with open("script/settings.py","w") as f:
		f.write(f"{file[:start]}{version}{file[end:]}")

# find the position of th version inside settings
with open("script/settings.py") as f:
	file = f.read()
version_define = file.index("=", file.index("self.version",file.index("def __init__"))) + 1
version = file[version_define:].replace(";","\n").split("\n")[0]
for i in version.split(" "):
	if i.isdigit(): 
		version_number = i
		break
version_define += version.index(version_number)
version_start_end = (version_define, version_define + len(version_number))

# ask for new version
if len(argv) == 1:
	user_input = input(f"what's the version? ({showVersion(int(version_number))})  ").strip()
else:
	user_input = argv[1]

# change the version if needed
if "." in user_input or user_input.isdigit():
	if "." in user_input:
		version_number = "".join([p.zfill(2)[:2] for p in user_input.split(".")])
	elif user_input.isdigit():
		version_number = user_input
	changeVersion(version_start_end[0],version_start_end[1], int(version_number))

# zip the program

def zip_file(include: list[str] = listdir(), name: str = osPath.basename(getcwd()), exclude: list[str] = []):
	if not name.endswith(".zip"): name += ".zip"
	zip_file = ZipFile(name, "x", compression=ZIP_DEFLATED, compresslevel=9)
	for i in include:
		if isdir(i):
			base_path = i.removesuffix(osPath.basename(i)) if len(include) > 1 else i
			for (path, dir, files) in walk(i):
				if not (path in exclude or osPath.basename(path) in exclude):
					for file in files:
						file_path = osPath.join(path, file)
						if not (file in exclude or file_path in exclude):
							zip_file.write(file_path,file_path.removeprefix(base_path))
		else:
			zip_file.write(i)

zip_name = osPath.basename(getcwd()) + "-V" + showVersion(int(version_number)) + ".zip"

for i in listdir():
	if i.endswith(".zip"): remove(i)
zip_file(["main.py","LICENSE","README.md","script"], zip_name, exclude=["__pycache__"])
