import os
# 自分(このファイル)のあるディレクトリを配信ルートにする。
# ミラー(scratchpad)側で実行されると、そのミラーを配信できる(Desktop直下はTCCで不可)。
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import http.server, socketserver

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

with socketserver.TCPServer(('127.0.0.1', 4173), Handler) as httpd:
    print('serving on http://127.0.0.1:4173 from', os.getcwd())
    httpd.serve_forever()
