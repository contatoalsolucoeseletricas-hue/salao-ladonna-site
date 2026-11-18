# -*- coding: utf-8 -*-
import http.server
import socketserver
import os
import socket
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

PORT = 8085
DIRECTORY = os.path.dirname(os.path.abspath(__file__))


class SalaoAppHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()


class ThreadedHTTPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


if __name__ == "__main__":
    local_ip = get_local_ip()
    print("=" * 65)
    print("LA DONNA STUDIO — HAIR & NAILS — SERVIDOR MULTI-THREAD ONLINE")
    print("=" * 65)
    print(f"No computador: http://localhost:{PORT}/index.html")
    print(f"No celular (mesmo Wi-Fi): http://{local_ip}:{PORT}/index.html")
    print("=" * 65)

    with ThreadedHTTPServer(("", PORT), SalaoAppHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor encerrado.")
