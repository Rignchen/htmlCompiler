from json import load, dump
from datetime import datetime, timedelta
from os import walk

class compiler:
	def __init__(self, settings):
		self.settings = settings.get
	def start(self):
		print("\033[94mLooking for files to compile...\033[0m")
		# compile all the files from the subfolder "run"
		for (path, dirs, files) in walk("run"):
			for file in files:
				filePath = f"{path}/{file}"
				self.compile(filePath)
	def compile(self, filePath: str):
		print(f"Compiling {filePath}...")