import csv
# from http.server import HTTPServer, BaseHTTPRequestHandler  

# class HTTPHandler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         self.send_response(200)
#         self.end_headers()
#         with open('ratings.csv') as f:
#             reader = csv.reader(f)
#             self.wfile.write(b"\n".join([','.join(row).encode() for row in reader]))

# httpd = HTTPServer(('localhost', 8081), HTTPHandler)
# httpd.serve_forever()

# curl localhost:8081