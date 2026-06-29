from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"Hello from Effective Mobile!")
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    port = int(os.getenv('BACKEND_PORT', 8080))
    server = HTTPServer(('0.0.0.0', port), Handler)
    print(f"Сервер запущен на порту {port}")
    server.serve_forever()