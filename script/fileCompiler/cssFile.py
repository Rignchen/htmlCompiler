from script.fileCompiler.css.insertion import insertion
from script.lib.basic import removeComments

def compileCss(fileContent: str) -> str:
	fileContent = removeComments(fileContent,"/*","*/")
	fileContent = insertion(fileContent)
	return formatCss(fileContent)
def formatCss(fileContent: str) -> str:
	content = [i.split("{") for i in fileContent.split("}")[:-1]]
	
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
	
	return "\n".join([i[0] + " {" + i[1] + "}" for i in content])
