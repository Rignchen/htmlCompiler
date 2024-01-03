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
	"""
	Replace the / by \\ on windows, do the opposite on linux
	"""
	return path.replace("/","\\") if osName == 'nt' else path.replace("\\","/")
def parseStr(content: str, maxSplit: int = -1) -> list[str]:
	"""
	Split the content around string separator
	"""
	temp = escapeSplit(content,'"',maxSplit*2)
	if len(temp)%2 == 0: raise SyntaxError("String not closed")
	return temp
def escapeSplit(content: str, character: str, maxSplit: int = -1):
	"""
	Split the content around character only if this character isn't escaped
	"""
	esc = False
	escLast = False
	out = [""]
	for i in range(len(content)):
		if content[i] == "\\":
			esc = True
		if content[i] == character and not escLast:
			maxSplit -= 1
			if maxSplit == 0:
				out.append(content[i+1:])
				break
			else: out.append("")
		else:
			out[-1] += content[i]
		
		if esc:
			if escLast: escLast = False
			else: escLast = True
		else: escLast = False
		esc = False
	return out
