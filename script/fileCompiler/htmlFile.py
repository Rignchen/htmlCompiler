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
	fileContent = fileContent.replace("\t","")
	fileContent = fileContent.replace(">",">\n").replace("<","\n<")
	fileContent = fileContent.removeprefix("\n").removesuffix("\n")
	while "\n\n" in fileContent: fileContent =  fileContent.replace("\n\n","\n")
	content = fileContent.split("\n")
	
	tab = 0
	out = []
	for line in content:
		if line.startswith("</"):
			tab = max(0, tab -1)
		out.append("\t" * tab + line)
		if line.startswith("<") and not (line.startswith("<!") or line.startswith("<meta") or line.startswith("<input") or line.startswith("<link") or line.startswith("</") or line.endswith("/>")):
			tab += 1
	return "\n".join(out)
