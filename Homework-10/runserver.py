import http.server as hs

Handler = hs.CGIHTTPRequestHandler
with hs.HTTPServer(('', 8000), Handler) as httpd:
    httpd.serve_forever()