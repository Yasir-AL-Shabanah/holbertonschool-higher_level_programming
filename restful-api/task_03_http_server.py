#!/usr/bin/python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="text/plain"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.end_headers()
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self._send(200, "Hello, this is a simple API!")
            return

        if self.path == "/status":
            self._send(200, "OK")
            return

        if self.path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            self._send(
                200,
                json.dumps(payload),
                "application/json"
            )
            return

        if self.path == "/info":
            payload = {"version": "1.0", "description": "A simple API built with http.server"}
            self._send(
                200,
                json.dumps(payload),
                "application/json"
            )
            return

        self._send(404, "Endpoint not found")

    def log_message(self, fmt, *args):
        return


def run():
    server = HTTPServer(("0.0.0.0", 8000), SimpleAPIHandler)
    server.serve_forever()


if __name__ == "__main__":
    run()
