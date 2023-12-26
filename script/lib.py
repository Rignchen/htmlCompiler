from genericpath import isdir
from os import getcwd, listdir, path as osPath, walk
from zipfile import ZipFile, ZIP_DEFLATED

def alignText(text: list[str], split: str, join:str = None) -> str:
	"""
	Aligns each element in the strings to the element above it.
	"""
	if join is None: join = split
	splitText = [i.split(split) for i in text]
	out: list[list[str]] = []
	size = len(splitText[0])
	for i in splitText: 
		if len(i) != size: raise ValueError("All lines must have the same number of elements")
		out.append([])
	for i in range(size):
		max = 0
		for j in splitText:
			if len(j[i]) > max: max = len(j[i])
		for j in range(len(splitText)):
			out[j].append(splitText[j][i].ljust(max))
	return "\n".join([join.join(i) for i in out])
def sec2hours(sec: int) -> str:
	"""
	Converts seconds to days, hours, minutes and seconds.
	"""
	if sec < 0: return f"-{sec2hours(-sec)}"
	if sec >= 86400: return f"{sec // 86400}d {sec2hours(sec % 86400)}"
	if sec >= 3600: return f"{sec // 3600}h {sec2hours(sec % 3600)}"
	if sec >= 60: return f"{sec // 60}m {sec2hours(sec % 60)}"
	if sec > 0: return f"{sec}s"
	return ""
def readVersion(version: int) -> str:
	"""
	display the version number in a readable format: mm.ss.ff
	"""
	main = version // 10000
	sub = (version - main * 10000) // 100
	fix = version - main * 10000 - sub * 100
	return f"{main}.{sub}.{fix}"
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
