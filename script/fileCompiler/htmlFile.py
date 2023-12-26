from script.fileCompiler.html.model import applyModel

def compileHTML(fileContent: str, filePath: str, models: dict[str,str]) -> str:
	fileContent = removeComments(fileContent)
	fileContent = applyModel(fileContent, filePath, models)
	return fileContent
def removeComments(fileContent: str) -> str:
	while "<!--" in fileContent:
		fileContent = fileContent[:fileContent.index("<!--")] + fileContent[fileContent.index("-->")+3:]
	return fileContent
