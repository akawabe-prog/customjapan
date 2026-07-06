import os
os.chdir('/Users/cjmac002/Desktop/CustomJapan_ReBranding')
import http.server, socketserver

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

with socketserver.TCPServer(('127.0.0.1', 4173), Handler) as httpd:
    print('serving on http://127.0.0.1:4173')
    httpd.serve_forever()
