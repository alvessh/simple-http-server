import http.server
import socketserver

PORT = 3002

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Servindo em http://localhost:" + str(PORT))
    httpd.serve_forever()
