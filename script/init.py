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
