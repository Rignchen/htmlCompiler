from script.lib.basic import correctPath

def applyModel(fileContent: str, filePath: str, models: dict[str,str]) -> str:
	fileContent = fileContent.replace("<pass/>","<model><model/></model>")
	if "<model>" in fileContent: 
		return pasteModel(getModel(models,filePath),splitModels(fileContent))
	return fileContent

def splitModels(fileContent: str) -> list[str]:
	models = [model.split("</model>")[0] for model in fileContent.split("<model>")]
	return models[1:] if len(models) > 1 else models
def getModel(modelList: dict[str,list[str]], filePath: str) -> str:
	path = filePath.split(correctPath("/"))
	is_model = path.pop() == "model.html"
	for i in range(len(path),0,-1):
		currentPath = correctPath("/").join(path[:i-1 if is_model else i])
		if currentPath in modelList:
			return modelList[currentPath]
def pasteModel(model: str, contents: list[str]) -> str:
	model: list[str] = model.split("<model/>")
	for i in range(len(contents)):
		if len(model) == 1: break
		model = [model.pop(0) + contents[i] + model.pop(0)] + model
	return "".join(model)
