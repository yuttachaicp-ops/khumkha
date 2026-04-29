import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8000))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Service-Worker-Allowed", "/")
        super().end_headers()

    def do_GET(self):
        if self.path == "/" or not os.path.exists(self.path.lstrip("/")):
            self.path = "/index.html"
        return super().do_GET()

    def log_message(self, format, *args):
        pass

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running on port {PORT}")
    httpd.serve_forever()
