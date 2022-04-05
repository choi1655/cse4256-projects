import urllib.request as url
import urllib.parse

req = url.Request("http://localhost:8000")
with url.urlopen(req) as response:
    html = response.read().decode("utf-8")
    print(f"Status {response.status}: {response.reason}")
    print(response.getheaders())
    print(html)

cgi_req = url.Request("http://localhost:8000/cgi-bin/playgame.py")
cgi_req.data = urllib.parse.urlencode({"fname":"Alan","lname":"Weide","thefile":None}).encode("ascii")
with url.urlopen(cgi_req) as response:
    html = response.read().decode("utf-8")
    print(f"Status {response.status}: {response.reason}")
    print(response.headers)
    print(html)