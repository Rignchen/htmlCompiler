from json import load, dump
from datetime import datetime, timedelta
from os import makedirs, walk, path as osPath, remove
from shutil import copy
from script.fileCompiler.htmlFile import compileHTML

class compiler:
	def __init__(self, settings):
		self.settings = settings.get
		self.models = {}
		with open("htmlCompilerCache.json", "r") as f:
			self.cache: dict[str,str|bool] = load(f)
	def save(self):
		with open("htmlCompilerCache.json", "w") as f:
			dump(self.cache, f, indent="\t")
	def start(self):
		print("\033[94mStart compiler...\033[0m")
		while self.settings["autoCompile"]:
			end = datetime.now() + timedelta(seconds=self.settings["compileDelay"])
			self.test_compile()
			while datetime.now() < end: pass
		else:
			self.test_compile()
	def test_compile(self):
		print("\r\033[94mChecking for changes...\033[0m",end="")
		# compile all the files from the subfolder "run" if they changed
		self.change = False
		cacheCopy = self.cache.copy()
		for cacheFile in cacheCopy:
			if not osPath.exists(cacheFile):
				self.change = True
				print(f"\nDeleting {cacheFile}...",end="")
				remove(f"compiled/{cacheFile.removeprefix('run/')}")
				del self.cache[cacheFile]
		for (path, dirs, files) in walk("run"):
			if "model.html" in files:
				self.compilePath(osPath.join(path, "model.html"))
			for file in files:
				if file == "model.html": continue
				self.compilePath(osPath.join(path, file))
		if self.change:
			print()
			self.save()
		else:
			print("\r\033[91mNo changes detected    \033[0m",end="")
	def compilePath(self, filePath: str):
		try:
			with open(filePath, "r") as f:
				fileContent = f.read()
		except UnicodeDecodeError:
			with open(filePath, "rb") as f:
				fileContent = str(f.read())
		if filePath in self.cache:
			if self.cache[filePath] != fileContent:
				self.compileFile(filePath,fileContent)
		else:
			self.compileFile(filePath,fileContent)
	def compileFile(self, filePath: str, fileContent: str):
		self.change = True
		print(f"\nCompiling {filePath}...",end="")
		self.cache[filePath] = fileContent

		compiledFilePath = f"compiled/{filePath.removeprefix('run/')}"
		makedirs(osPath.dirname(compiledFilePath), exist_ok=True)

		match filePath.split(".")[-1]:
			case "html":
				compiled = compileHTML(fileContent,filePath,self.models)
				if osPath.basename(filePath) == "model.html":
					self.models[filePath.removesuffix("/model.html")] = compiled
				else:
					with open(compiledFilePath, "w") as f:
						f.write(compiled)
			case _:
				copy(filePath, compiledFilePath)

