def insertion(fileContent: str) -> str:
	out, parsed = parse(fileContent)
	for selectors, content in parsed:
		out += glue_selectors(selectors) + "{" + content + "}"
	return out
def parse(fileContent: str) -> tuple[list[tuple[list[str], str]],str]:
	"""
	parse the given content\n\n

	return a tuple wich contain a string and list of tuple\n
	the string contains all the css that's outside balises
	each of the tuple in the list are composed of a list and the content of the selector\n
	this list is composed of string wich are 
	"""

	out: list[tuple[list[str], str]] = []
	selector: list[str] = []
	content: list[str] = []
	inBlock = 0
	outside = ""

	current = ""

	for i in fileContent:
		match i:
			case ";":
				if inBlock:
					content[-1] += current + ";"
				else:
					outside += current + ";"
				current = ""
			case "{":
				inBlock += 1
				content.append("")
				selector.append(current)
				current = ""
			case "}":
				inBlock -= 1
				content[-1] += current
				out.append((selector.copy(),content[-1]))
				selector.pop()
				content.pop()
			case _:
				current += i
	
	out.reverse()
	return outside, out 
def glue_selectors(selectors: list[str]) -> str:
	out = selectors.pop(0).split(",")
	for i in selectors:
		new = []
		for j in out:
			for k in i.split(","):
				addition = k.strip()
				if not addition.startswith(":"): addition = " " + addition
				new.append(j.strip() + addition)
		out = new
	return ",".join(out)
