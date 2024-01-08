from json import dump
from os import mkdir, listdir, system
from script.fileCompiler.htmlFile import formatHtml
from script.fileCompiler.cssFile import formatCss

# set the default settings
settings = {
	"autoCompile": True,
	"compileDelay": 10, # seconds
	# add settings here
}

# create the .json file
with open("htmlCompilerCache.json", "w") as f:
	f.write("{}")
with open("htmlCompilerModelsCache.json", "w") as f:
	f.write("{}")
with open("htmlCompilerSettings.json", "w") as f:
	dump(settings, f, indent="\t")

# create the run and compiled folder
if not "run" in listdir():
	mkdir("run")
if not "compiled" in listdir():
	mkdir("compiled")

# add the html exemple files
with open("run/model.html", "w") as f:
	f.write(formatHtml("".join([
		'<!DOCTYPE html><html lang="en">',
		'<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><model/><!-- this first model is here to add stuff in the head balise --><title>Document</title></head>',
		'<body><model/><!-- this second model is the main content of the page --></body></html>'
	])))
with open("run/index.html", "w") as f:
	f.write(formatHtml("".join([
		'<model><link rel="stylesheet" href="style.css"></model>',
		'<model><h1>Hello World</h1></model>'
	])))
with open("run/style.css", "w") as f:
	f.write(formatCss('h1{text-align:center;font-size:10em;}'))

# create the gitignore file and git repo
with open(".gitignore", "w") as f:
	f.write("\n".join([
		"compiled/",
		"htmlCompilerCache.json",
		"htmlCompilerModelsCache.json",
		"htmlCompilerSettings.json",
		"null"
	]))
system("git init")
