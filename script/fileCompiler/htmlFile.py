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
			if content[line].split(" ")[0].replace("<","</",1) in "".join(content[line:]):
				tab += 1
	return "\n".join(out)
