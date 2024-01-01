from os import system, name as osName

def cls():
	"""Clear the shell"""
	system("cls" if osName == 'nt' else "clear")
def alignText(text: list[str], split: str, join:str = None) -> str:
	"""
	Aligns each element in the strings to the element above it.
	"""
	if join is None: join = split
	splitText = [i.split(split) for i in text]
	out: list[list[str]] = []
	size = len(splitText[0])
	for i in splitText: 
		if len(i) != size: 
			raise ValueError(f"All lines must have the same number of elements but found {size} in {text[0]} and {len(i)} in {split.join(i)}")
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
def removeComments(fileContent: str, commentStart: str, commentEnd: str):
	"""
	Remove everything that start with commentStart and end with commentEnd inside fileContent
	"""
	index = 0
	while(commentStart in fileContent and commentEnd in fileContent):
		index = fileContent.index(commentStart, index)
		endIndex = fileContent.index(commentEnd, index) + len(commentEnd)
		fileContent = fileContent[:index] + fileContent[endIndex:]
	return fileContent
def correctPath(path: str) -> str:
	return path.replace("/","\\") if osName == 'nt' else path.replace("\\","/")
