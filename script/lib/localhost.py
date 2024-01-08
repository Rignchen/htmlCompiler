from http.server import SimpleHTTPRequestHandler
from os import name as osName
from socketserver import TCPServer
import sys
from threading import Thread

class _CustomHttpHandler(SimpleHTTPRequestHandler):
	dir: str = "."
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs, directory=self.dir)
class localhostThread(Thread):
	def __init__(self, directory: str = ".", port: int = 8000, force_port: bool = False, pipe: list|None = None):
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
def sendMessage(message, pipe: list|None = None):
	if pipe == None: print(message)
	else: pipe.append(message)
def printMessage(pipe: list = None, min_message: int = 0):
	while len(pipe) < min_message: pass
	while len(pipe) > 0: print(pipe.pop(0))
def startLocalhost(directory: str = ".", port: int = 8000, force_port: bool = False) -> tuple[Thread, list]:
	"""
	Start a new localhost on a new Thread\n
	It return the process and pipe used for the localhost, both of them are needed to stop this one
	"""
	pipe = []
	process = localhostThread(directory, port, force_port, pipe)
	process.start()
	printMessage(pipe, 1)
	return process, pipe
def stopLocalhost(localhost: tuple[localhostThread, list]) -> None:
	"""
	Stop a thread with the localhost\n
	The input is the return of startLcalhost()
	"""
	process, pipe = localhost
	print("Shutting down host, this may take a few minutes")
	process.stop()
	printMessage(pipe)
