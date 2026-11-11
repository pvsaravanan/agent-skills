"""Static server without caching.

The built-in http.server lets the browser cache JS modules heuristically,
so edits to the timeline/scenes sometimes do not show after a normal reload.
Cache-Control: no-store forces the browser to fetch fresh files every time.

Usage:  python tools/serve.py   (port 5178)
"""
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5178

class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

    def log_message(self, *args):
        pass  # silent; request logs are not useful here

if __name__ == '__main__':
    print(f'serving on http://127.0.0.1:{PORT} (no-store)')
    ThreadingHTTPServer(('127.0.0.1', PORT), NoCacheHandler).serve_forever()
