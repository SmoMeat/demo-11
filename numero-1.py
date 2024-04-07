import http.server


class WebServer(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        doc = open('numero-1.html').read()

        self.send_response(200)
        self.end_headers()
        self.wfile.write(doc.encode('utf-8'))

    def log_message(self, format, *args):
        pass

http.server.HTTPServer(('localhost', 8000), WebServer).serve_forever()
