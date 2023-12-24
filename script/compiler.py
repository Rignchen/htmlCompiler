from json import load, dump
from datetime import datetime, timedelta
from os import makedirs, walk, path as osPath, remove
from shutil import copy

class compiler:
	def __init__(self, settings):
		self.settings = settings.get
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
			for file in files:
				filePath = f"{path}/{file}"
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
		if self.change:
			print()
			self.save()
		else:
			print("\r\033[91mNo changes detected    \033[0m",end="")
	def compileFile(self, filePath: str, fileContent: str):
		self.change = True
		print(f"\nCompiling {filePath}...",end="")
		self.cache[filePath] = fileContent

		compiledFilePath = f"compiled/{filePath.removeprefix('run/')}"
		makedirs(osPath.dirname(compiledFilePath), exist_ok=True)

		match filePath.split(".")[-1]:
			case _:
				copy(filePath, compiledFilePath)
