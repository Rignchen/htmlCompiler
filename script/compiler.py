from json import load, dump
from datetime import datetime, timedelta
from os import makedirs, walk, path as osPath, remove
from shutil import copy
from script.fileCompiler.cssFile import compileCss
from script.fileCompiler.htmlFile import compileHTML
from script.lib.basic import correctPath

class compiler:
	def __init__(self, settings):
		self.settings = settings
		self.fail = 0
		with open("htmlCompilerModelsCache.json", "r") as f:
			self.models: dict[str,str] = load(f)
		with open("htmlCompilerCache.json", "r") as f:
			self.cache: dict[str,str] = load(f)
	def saveCache(self):
		with open("htmlCompilerCache.json", "w") as f:
			dump(self.cache, f, indent="\t")
	def saveModels(self):
		with open("htmlCompilerModelsCache.json", "w") as f:
			dump(self.models, f, indent="\t")
	def start(self):
		print("\033[94mStart compiler...\033[0m")
		while self.settings.get["autoCompile"]:
			end = datetime.now() + timedelta(seconds=self.settings.get["compileDelay"])
			self.test_compile()
			while datetime.now() < end: pass
		else:
			self.test_compile()
			print()
	def test_compile(self):
		print("\r\033[94mChecking for changes...   \033[0m",end="")
		# compile all the files from the subfolder "run" if they changed
		self.change = False
		self.changeModels = []
		cacheCopy = self.cache.copy()
		for cacheFile in cacheCopy:
			if not osPath.exists(cacheFile):
				self.change = True
				print(f"\nDeleting {cacheFile}...",end="")
				if cacheFile.endswith(correctPath("/model.html")):
					model = cacheFile.removesuffix(correctPath("/model.html"))
					del self.models[model]
					self.actualiseModels(model)
				else: remove(f"compiled/{cacheFile.removeprefix(correctPath('run/'))}")
				try:
					del self.cache[cacheFile]
				except KeyError: # the file has allready been removed
					pass
		for (path, dirs, files) in walk("run"):
			if "model.html" in files:
				self.compilePath(osPath.join(path, "model.html"))
			for file in files:
				if file == "model.html": continue
				self.compilePath(osPath.join(path, file))
		if self.change:
			self.fail = 0
			print()
			if self.changeModels:
				self.saveModels()
			self.saveCache()
		else:
			print(f"\r\033[91mNo changes detected {f'({self.fail})' if self.fail > 0 else 3*' '}\033[0m",end="")
			self.fail += 1
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

		compiledFilePath = f"compiled/{filePath.removeprefix(correctPath('run/'))}"
		makedirs(osPath.dirname(compiledFilePath), exist_ok=True)

		match filePath.split(".")[-1]:
			case "html":
				try:
					compiled = compileHTML(fileContent,filePath,self.models)
				except:
					if self.settings.param["compilerDebug"]: raise
					print(f"\r\033[91mUnable to compile {filePath}",end="")
					return
				if osPath.basename(filePath) == "model.html":
					model = filePath.removesuffix(correctPath("/model.html"))
					self.actualiseModels(model)
					self.models[model] = compiled
				else:
					with open(compiledFilePath, "w") as f:
						f.write(compiled)
			case "css":
				try:
					compiled = compileCss(fileContent)
				except:
					if self.settings.param["compilerDebug"]: raise
					print(f"\r\033[91mUnable to compile {filePath}",end="")
					return
				with open(compiledFilePath, "w") as f:
					f.write(compiled)
			case _:
				copy(filePath, compiledFilePath)
	def actualiseModels(self, modelName: str):
		if self.changeModels:return
		cachCopy = self.cache.copy()
		for file in cachCopy:
			if file.startswith(modelName) and file != modelName + correctPath("/model.html"): del self.cache[file]
		self.changeModels = True

