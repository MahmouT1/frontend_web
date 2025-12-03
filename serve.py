#!/usr/bin/env python3
"""
Simple HTTP server for Frontend development
Solves CORS issues when opening HTML files directly (file://)
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

PORT = 3000
DIRECTORY = Path(__file__).parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)
    
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-API-Key')
        super().end_headers()

def main():
    os.chdir(DIRECTORY)
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}/index-optimized.html"
        print("\n" + "=" * 60)
        print("🌐 Frontend Server Started!")
        print("=" * 60)
        print(f"📍 Server: http://localhost:{PORT}")
        print(f"🔗 Open: {url}")
        print("=" * 60)
        print("\nPress Ctrl+C to stop the server\n")
        
        # Auto-open browser
        try:
            webbrowser.open(url)
        except:
            pass
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✅ Server stopped.")

if __name__ == "__main__":
    main()

