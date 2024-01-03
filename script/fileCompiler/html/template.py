from script.lib.basic import parseStr, escapeSplit

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

def glueTemplate(fileContent: str, name: str, template: str) -> str:
	templateName = f"template-{name}"
	while f"<{templateName}" in fileContent:
		fileContent, args = parseTemplateArguments(fileContent, templateName)
		temp = fileContent.split(f"<{templateName}>",1)
		fileContent = temp[0] + fillTemplate(template, args) + temp[1]
	return fileContent
def parseTemplateArguments(fileContent: str, templateName: str) -> tuple[str,str]:
	temp = fileContent.split(f"<{templateName}",1)
	if "args" in temp[1].split(">")[0]: #arguments have been set
		temp = temp + parseStr(temp.pop(),1)
		args = temp[2]
	else: args = ""
	fileContent = temp[0] + f"<{templateName}" + temp[-1][1:]
	return fileContent, args

def fillTemplate(template: str, args: str) -> str:
	templatesPart = template.split("<arg/>")
	argsPart = escapeSplit(args,";")
	content = templatesPart.pop(0)
	while len(templatesPart) > 0:
		if len(argsPart) > 0:
			content += argsPart.pop(0) + templatesPart.pop(0)
		else:
			content += ''.join(templatesPart)
			break
	return content

def applyTemplates(fileContent: str, templates: dict[str, str] = {}) -> str:
	fileContent, templates = parseTemplates(fileContent, templates)
	for name in templates:
		fileContent = glueTemplate(fileContent, name, templates[name])
	return fileContent
