#!/usr/bin/env python3
"""Maze Website Launcher — starts a local server and opens the browser."""
import http.server
import webbrowser
import threading
import os
import socket

PORT = 8765

def get_site_dir():
    return os.path.dirname(os.path.abspath(__file__))

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def main():
    site_dir = get_site_dir()
    os.chdir(site_dir)

    handler = http.server.SimpleHTTPRequestHandler
    server = http.server.HTTPServer(('0.0.0.0', PORT), handler)

    local_url = f'http://127.0.0.1:{PORT}/cover.html'
    lan_ip = get_local_ip()
    lan_url = f'http://{lan_ip}:{PORT}/cover.html'

    print(f'  Local:   {local_url}')
    print(f'  Network: {lan_url}  (open on phone/tablet)')

    threading.Timer(0.8, lambda: webbrowser.open(local_url)).start()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down.')
        server.shutdown()

if __name__ == '__main__':
    main()
