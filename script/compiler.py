from json import load, dump
from datetime import datetime, timedelta
from os import walk, path as osPath

class compiler:
	def __init__(self, settings):
		self.settings = settings.get
		with open("htmlCompilerCache.json", "r") as f:
			self.cache = load(f)
	def save(self):
		with open("htmlCompilerCache.json", "w") as f:
			dump(self.cache, f, indent="\t")
	def start(self):
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
				del self.cache[cacheFile]
		for (path, dirs, files) in walk("run"):
			for file in files:
				filePath = f"{path}/{file}"
				with open(filePath, "r") as f:
					fileContent = f.read()
				if filePath in self.cache:
					if self.cache[filePath] != fileContent:
						self.compile(filePath,fileContent)
				else:
					self.compile(filePath,fileContent)
		if self.change:
			print()
			self.save()
		else:
			print("\r\033[91mNo changes detected    \033[0m",end="")
	def compile(self, filePath: str, fileContent: str):
		self.change = True
		print(f"\nCompiling {filePath}...",end="")
		self.cache[filePath] = fileContent
