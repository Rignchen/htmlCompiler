def compileHTML(fileContent, filePath, models):
	modelList = getModelList(models, filePath)
def compileModels(fileContent: str) -> list[str]:
	return [fileContent]
def removeComments(fileContent: str) -> str:
	while "<!--" in fileContent:
		fileContent = fileContent[:fileContent.index("<!--")] + fileContent[fileContent.index("-->")+3:]
	return fileContent
def getModelList(modelList: dict[str,list[str]], filePath: str) -> list[list[str]]:
	path = filePath.replace("\\","/").split("/")
	pathList: list[list[str]] = []
	for i in range(len(path)-1,-1,-1):
		currentPath = "/".join(path[:i+1])
		if currentPath in modelList:
			pathList.append(modelList[currentPath])
			# find the last model where the list has a length of 1
			if len(pathList[-1]) == 1: 
				pathList.reverse()
				return pathList
def pasteModel(content: str, model: list[str]) -> str:
	content: list[str] = content.split("<model/>")
	for i in range(len(model)):
		if len(content) == 1: break
		content = [content.pop(0) + model[i] + content.pop(0)] + content
	return "".join(content)
