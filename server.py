#!/usr/bin/env python3
import http.server
import mimetypes

# Ensure PDF is served with the correct MIME type
mimetypes.add_type('application/pdf', '.pdf')
mimetypes.add_type('image/jpeg', '.jpg')
mimetypes.add_type('image/jpeg', '.jpeg')
mimetypes.add_type('image/png', '.png')

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Allow PDF download and viewing in browser
        if self.path.endswith('.pdf'):
            self.send_header('Content-Type', 'application/pdf')
            self.send_header('Content-Disposition', 'attachment')
        super().end_headers()

    def log_message(self, format, *args):
        pass  # suppress logs

if __name__ == '__main__':
    import os
    os.chdir('/Users/saipuneeth/portfolio')
    server = http.server.HTTPServer(('', 8080), Handler)
    print("Server running at http://localhost:8080/portfolio.html")
    server.serve_forever()
