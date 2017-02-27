
import http.server
import socketserver
import io


class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Hey Dude...</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a CI PoC!</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


print('Server listening on port 8080...')
httpd = socketserver.TCPServer(('', 8080), Handler)
httpd.serve_forever()

