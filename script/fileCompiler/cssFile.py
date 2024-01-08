from script.fileCompiler.css.insertion import insertion
from script.lib.basic import removeComments

def compileCss(fileContent: str) -> str:
	fileContent = removeComments(fileContent,"/*","*/")
	fileContent = insertion(fileContent)
	return formatCss(fileContent)
def formatCss(fileContent: str) -> str:
	last_colomn = 0
	for i in range(len(fileContent)):
		match fileContent[i]:
			case ";": last_colomn = i
			case "{": break
	if last_colomn:
		last_colomn += 1
		out = fileContent[:last_colomn]
		out += "\n"
	else: out = ""

	content = [i.split("{") for i in fileContent[last_colomn:].split("}")[:-1]]
	
	i = 0
	while i < len(content):
		content[i] = [
			",\n".join([j.strip() for j in content[i][0].split(",")]),
			"\n\t" + ";\n\t".join(["".join([k.strip() for k in j.split("\n")]) for j in content[i][1].split(";")])[:-1]
		]
		if content[i][1] == "\n\t":
			content.pop(i)
			continue
		i += 1
	
	return out + "\n".join([i[0] + " {" + i[1] + "}" for i in content])
