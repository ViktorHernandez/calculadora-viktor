import http.server
import socketserver
import os

PORT = 8080
DIR = os.path.join(os.path.dirname(__file__), "app")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def log_message(self, format, *args):
        print(f"[{self.log_date_time_string()}] {format % args}")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Servidor corriendo en http://localhost:{PORT}")
        print("Presiona Ctrl+C para detener")
        httpd.serve_forever()
