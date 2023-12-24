def align(text: list[str], split: str, join:str = None) -> str:
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
	Converts seconds to hours, minutes and seconds.
	"""
	if sec == 0: return "0s"
	elif sec < 0: return f"-{sec2hours(-sec)}"
	hours = sec // 3600
	minutes = (sec - hours * 3600) // 60
	seconds = sec - hours * 3600 - minutes * 60
	out = ""
	if hours > 0: out += f"{hours}h "
	if minutes > 0: out += f"{minutes}m "
	if seconds > 0: out += f"{seconds}s"
	return out
def readVersion(version: int) -> str:
	"""
	display the version number in a readable format: mm.ss.ff
	"""
	main = version // 10000
	sub = (version - main * 10000) // 100
	fix = version - main * 10000 - sub * 100
	return f"{main}.{sub}.{fix}"
