from script.lib.basic import removeComments

def compileCss(fileContent: str) -> str:
	fileContent = removeComments(fileContent,"/*","*/")
	return formatCss(fileContent)
def formatCss(fileContent: str):
	return fileContent