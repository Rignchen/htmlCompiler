from script.fileCompiler.html.model import applyModel

def compileHTML(fileContent: str, filePath: str, models: dict[str,str]) -> str:
	fileContent = removeComments(fileContent)
	fileContent = applyModel(fileContent, filePath, models)
	return formatHtml(fileContent)
def removeComments(fileContent: str) -> str:
	while "<!--" in fileContent:
		fileContent = fileContent[:fileContent.index("<!--")] + fileContent[fileContent.index("-->")+3:]
	return fileContent
def formatHtml(fileContent: str):
	closeBalise = []
	dontCloseBalise = []

	fileContent = fileContent.replace(">",">\n").replace("<","\n<")
	fileContent = fileContent.removeprefix("\n").removesuffix("\n")
	content = [file.strip() for file in fileContent.split("\n")]
	while "" in content: content.remove("")
	
	tab = 0
	out = []
	for line in range(len(content)):
		if content[line].startswith("</"):
			tab = max(0, tab -1)
		out.append("\t" * tab + content[line])
		if content[line].startswith("<") and not (content[line].startswith("</") or content[line].endswith("/>")):
			balise = content[line].split(" ")[0].removesuffix(">")
			if not (balise in closeBalise or balise in dontCloseBalise):
				if balise.replace("<","</",1) in "".join(content[line:]): closeBalise.append(balise)
				else:dontCloseBalise.append(balise)
			if balise in closeBalise: tab += 1
	return "\n".join(out)
