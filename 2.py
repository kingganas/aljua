from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

# Directory containing HLS files
STREAM_DIR = "stream"
os.makedirs(STREAM_DIR, exist_ok=True)


class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        # Handle CORS preflight requests
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        # Serve files from STREAM_DIR
        self.directory = STREAM_DIR
        super().do_GET()


if __name__ == "__main__":
    PORT = 8080
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, CustomHandler)
    print(f"Serving HTTP on port {PORT}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
        httpd.server_close()
