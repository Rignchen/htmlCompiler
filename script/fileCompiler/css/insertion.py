def insertion(fileContent: str) -> str:
	return fileContent
def parse(fileContent: str) -> list[tuple[list[str], str]]:
	"""
	parse the given content\n\n

	return a list of tuple\n
	each of the tuple are composed of a list and the content of the selector\n
	this list is composed of string wich are 
	"""

	out: list[tuple[list[str], str]] = []
	selector: list[str] = []
	content: list[str] = []

	current = ""

	for i in fileContent:
		match i:
			case ";":
				content[-1] += current + ";"
				current = ""
			case "{":
				content.append("")
				selector.append(current)
				current = ""
			case "}":
				content[-1] += current
				out.append((selector.copy(),content[-1]))
				selector.pop()
				content.pop()
			case _:
				current += i
	
	out.reverse()
	return out
