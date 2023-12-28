from http.server import SimpleHTTPRequestHandler
from multiprocessing import Process, Pipe
from socketserver import TCPServer

class _CustomHttpHandler(SimpleHTTPRequestHandler):
	dir: str = "."
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs, directory=self.dir)

def _sendMessage(message, pipe: any = None):
	if pipe == None: print(message)
	else: pipe.send(message)
def _localhostLaunch(port: int, handler, pipe: any) -> None:
	with TCPServer(("", port), handler) as httpd:
		_sendMessage(f"Starting localhost on http://localhost:{port}", pipe)
		try:
			httpd.serve_forever()
		except:
			_sendMessage("\nServer stopped.", pipe)
def localhost(directory: str = ".", port: int = 8000, force_port: bool = False, pipe: any = None) -> None:
	"""
	Start a new localhost\n
	This will use the whole thread, consider using the startLocalhost function to remediate
	"""
	handler = _CustomHttpHandler
	handler.dir = directory
	while True:
		try: 
			_localhostLaunch(port, handler, pipe)
			break
		except OSError:
			if force_port: raise
			port += 1
def startLocalhost(directory: str = ".", port: int = 8000, force_port: bool = False):
	"""
	Start a new localhost on a new Process\n
	It return the process and pipe used for the localhost, both of them are needed to stop this one
	"""
	parent_pipe, child_pipe = Pipe()
	process = Process(target=localhost,args=(directory, port, force_port, child_pipe))
	process.start()
	return process, parent_pipe
def stopLocalhost(localhost: tuple[Process, any]) -> None:
	"""
	Stop a thread with the localhost\n
	The input is the return of startLcalhost()
	"""
	process, pipe = localhost
	process.terminate()
