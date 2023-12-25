def compileHTML(fileContent, filePath, models):
	model = getModel(models, filePath)
	return fileContent
def compileModels(fileContent: str) -> list[str]:
	return [fileContent]
def getModel(modelList: dict[str,list[str]], filePath: str) -> str:
	return modelList[filePath][0]
def pasteModel(content: str, model: list[str]) -> str:
	content: list[str] = content.split("<model/>")
	for i in range(len(model)):
		if len(content) == 1: break
		content = [content.pop(0) + model[i] + content.pop(0)] + content
	return "".join(content)
