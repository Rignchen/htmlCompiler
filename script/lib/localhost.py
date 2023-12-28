from http.server import SimpleHTTPRequestHandler
from multiprocessing import Process
from socketserver import TCPServer

class _CustomHttpHandler(SimpleHTTPRequestHandler):
	dir: str = "."
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs, directory=self.dir)

def _localhostLaunch(port: int, handler) -> None:
	with TCPServer(("", port), handler) as httpd:
		print(f"Serving on http://localhost:{port}")
		try:
			httpd.serve_forever()
		except:
			print("\nServer stopped.")
def localhost(directory: str = ".", port: int = 8000, force_port: bool = False) -> None:
	"""
	Start a new localhost\n
	This will use the whole thread, consider using the startLocalhost function to remediate
	"""
	handler = _CustomHttpHandler
	handler.dir = directory
	while True:
		try: 
			_localhostLaunch(port, handler)
			break
		except OSError:
			if force_port: raise
			port += 1
def startLocalhost(directory: str = ".", port: int = 8000, force_port: bool = False):
	"""
	Start a new localhost on a new Process
	"""
	process = Process(target=localhost,args=(directory, port, force_port))
	process.start()
	return process
def stopLocalhost(localhost: Process) -> None:
	"""
	Stop a thread with the localhost\n
	The input is the return of startLcalhost()
	"""
	localhost.terminate()
