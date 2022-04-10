"""File: main.py
Author: John Choi choi.1655@osu.edu
Version: April 10, 2022

The Ohio State University CSE4256 SP22 Homework 10.

Right now, running this script throws an error: urllib.error.URLError: <urlopen error [Errno 61] Connection refused>
After researching online, I figured that it is happening because of my network settings which does not allow
such connections...but I could be wrong.
Running `python3 -m http.server --cgi` command outputs the correct file, however.
"""

import urllib.request as url
import urllib.parse

# req = url.Request("http://localhost:8000")
# with url.urlopen(req) as response:
#     html = response.read().decode("utf-8")
#     print(f"Status {response.status}: {response.reason}")
#     print(response.getheaders())
#     print(html)

cgi_req = url.Request("http://localhost:8000/cgi-bin/playgame.py")
cgi_req.data = urllib.parse.urlencode({"nplayers": 5}).encode("ascii")
with url.urlopen(cgi_req) as response:
    html = response.read().decode("utf-8")
    print(f"Status {response.status}: {response.reason}")
    print(response.headers)
    print(html)
