from http.server import SimpleHTTPRequestHandler
from multiprocessing import Process
from socketserver import TCPServer

class CustomHttpHandler(SimpleHTTPRequestHandler):
	dir: str = "."
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs, directory=self.dir)
def localhost(directory: str = ".", port: int = 8000, force_port: bool = False) -> None:
	handler = CustomHttpHandler
	handler.dir = directory
	while True:
		try: 
			localhostLaunch(port, handler)
			break
		except OSError:
			if force_port: raise
			port += 1
def localhostLaunch(port: int, handler) -> None:
	with TCPServer(("", port), handler) as httpd:
		print(f"Serving on http://localhost:{port}",flush=True)
		try:
			httpd.serve_forever()
		except:
			print("\nServer stopped.")
def startLocalhost(directory: str = ".", port: int = 8000, force_port: bool = False):
	process = Process(target=localhost,args=(directory, port, force_port))
	process.start()
	return process
