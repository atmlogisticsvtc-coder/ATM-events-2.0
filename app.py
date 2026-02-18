class Handler(BaseHTTPRequestHandler):
    def _ok(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()

    def do_GET(self):
        if self.path in ("/", "/healthz"):
            self._ok()
            self.wfile.write(b"ok")
        else:
            self.send_response(404)
            self.end_headers()

    def do_HEAD(self):
        if self.path in ("/", "/healthz"):
            self._ok()
        else:
            self.send_response(404)
            self.end_headers()
