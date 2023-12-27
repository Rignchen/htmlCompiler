from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

def localhost(port: int) -> None:
	handler = SimpleHTTPRequestHandler
	while True:
		try: 
			localhostLaunch(port, handler)
			break
		except OSError:
			port += 1
def localhostLaunch(port: int, handler) -> None:
	with TCPServer(("", port), handler) as httpd:
		print(f"Serving on http://localhost:{port}",flush=True)
		try:
			httpd.serve_forever()
		except:
			print("\nServer stopped.")