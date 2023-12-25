def compileHTML(fileContent: str, filePath: str, models: dict[str,str]) -> str:
	fileContent = removeComments(fileContent)
	if "<model>" in fileContent:
		return pasteModel(getModel(models,filePath),splitModels(fileContent))
	return fileContent
def removeComments(fileContent: str) -> str:
	while "<!--" in fileContent:
		fileContent = fileContent[:fileContent.index("<!--")] + fileContent[fileContent.index("-->")+3:]
	return fileContent

def splitModels(fileContent: str) -> list[str]:
	models = [model.split("</model>")[0] for model in fileContent.split("<model>")]
	return models[1:] if len(models) > 1 else models
def getModel(modelList: dict[str,list[str]], filePath: str) -> str:
	path = filePath.replace("\\","/").split("/")
	for i in range(len(path)-1,-1,-1):
		currentPath = "/".join(path[:i+1])
		if currentPath in modelList:
			return modelList[currentPath]
def pasteModel(model: str, contents: list[str]) -> str:
	model: list[str] = model.split("<model/>")
	for i in range(len(contents)):
		if len(model) == 1: break
		model = [model.pop(0) + contents[i] + model.pop(0)] + model
	return "".join(model)
