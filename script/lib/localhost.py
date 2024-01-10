from http.server import SimpleHTTPRequestHandler
from os import name as osName
from socketserver import TCPServer
import sys
from threading import Thread

class Pipe:
	def __init__(self):
		self._value = []
	def __len__(self):
		return len(self._value)
	def __iter__(self):
		yield self._value.pop(0)
	def send(self,value):
		self._value.append(value)
	def peak(self) -> list:
		return self._value
	def hasValues(self):
		return self.__len__() > 1

class _CustomHttpHandler(SimpleHTTPRequestHandler):
	dir: str = "."
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs, directory=self.dir)
class localhostThread(Thread):
	def __init__(self, directory: str = ".", port: int = 8000, force_port: bool = False, pipe: Pipe|None = None):
		"""
		Start a new localhost
		"""
		super().__init__()
		self.directory = directory
		self.port = port
		self.force_port = force_port
		self.pipe = pipe
		self.httpd = None
	def run(self):
		handler = _CustomHttpHandler
		handler.dir = self.directory
		while True:
			try: 
				self.localhostLaunch(handler)
				break
			except OSError:
				if self.force_port: raise
				self.port += 1
	def stop(self):
		if self.httpd != None:
			self.httpd.shutdown()
	def localhostLaunch(self, handler) -> None:
		self.httpd = TCPServer(("", self.port), handler)
		sendMessage(f"Starting localhost on http://localhost:{self.port}", self.pipe)
		try:
			sys.stderr = open("null" if osName == "nt" else "/dev/null", "w")
			self.httpd.serve_forever()
		finally:
			sendMessage("Localhost stopped", self.pipe)
def sendMessage(message, pipe: Pipe|None = None):
	if pipe == None: print(message)
	else: pipe.send(message)
def printMessage(pipe: Pipe, min_message: int = 1):
	while len(pipe) < min_message: pass
	for message in pipe:
		print(message)
def startLocalhost(directory: str = ".", port: int = 8000, force_port: bool = False) -> tuple[Thread, list]:
	"""
	Start a new localhost on a new Thread\n
	It return the process and pipe used for the localhost, both of them are needed to stop this one
	"""
	pipe = Pipe()
	process = localhostThread(directory, port, force_port, pipe)
	process.start()
	printMessage(pipe, 1)
	return process, pipe
def stopLocalhost(localhost: tuple[localhostThread, Pipe]) -> None:
	"""
	Stop a thread with the localhost\n
	The input is the return of startLcalhost()
	"""
	print("Shutting down host, this may take a few minutes")
	_stopLocalHost(*localhost)
async def _stopLocalHost(process: localhostThread, pipe: Pipe) -> None:
	process.stop()
	printMessage(pipe)
