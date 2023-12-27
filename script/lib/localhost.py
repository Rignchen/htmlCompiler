from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

def localhost(port: int) -> None:
	handler = SimpleHTTPRequestHandler
	with TCPServer(("", port), handler) as httpd:
		print(f"Serving on http://localhost:{port}",flush=True)
		try:
			httpd.serve_forever()
		except:
			print("\nServer stopped.")
