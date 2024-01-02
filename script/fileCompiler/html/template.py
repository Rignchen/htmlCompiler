from script.lib.basic import cls

def parseTemplates(fileContent: str, templates: dict[str, str] = {}) -> tuple[str, dict[str, str]]:
	while "<def-template-" in fileContent:
		temp = parse1Template(fileContent)
		fileContent = temp[0]
		templates[temp[1]] = temp[2]
	return fileContent, templates
def parse1Template(fileContent: str) -> tuple[str,str,str]:
	temp = fileContent.split("<def-template-",1)
	temp = temp + temp.pop().split(">", 1)
	temp = temp + temp.pop().split(f"</def-template-{temp[1]}>")
	return temp[0] + temp[-1], temp[1],temp[2]

def applyTemplate(fileContent: str, templates: dict[str, str] = {}) -> str:
	fileContent, templates = parseTemplates(fileContent, templates)
	return fileContent
