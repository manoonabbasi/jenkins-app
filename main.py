print("INFO: A HTTP Server...")

import http.server
import socketserver

# Define the port you want to use
port = 8888

# Create a simple HTTP server
with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Serving on port {port}")
    # Start the server
    httpd.serve_forever()
