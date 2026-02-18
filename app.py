import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import bot


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


def start_http_server():
    port = int(os.environ.get("PORT", "10000"))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()


def start_bot():
    bot.main()


if __name__ == "__main__":
    threading.Thread(target=start_bot, daemon=True).start()
    start_http_server()
