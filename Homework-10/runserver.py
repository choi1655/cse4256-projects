"""File: runserver.py
Author: John Choi choi.1655@osu.edu
Version: April 10, 2022

The Ohio State University CSE4256 SP22 Homework 10.
"""

import http.server as hs

Handler = hs.CGIHTTPRequestHandler
with hs.HTTPServer(('', 8000), Handler) as httpd:
    httpd.serve_forever()