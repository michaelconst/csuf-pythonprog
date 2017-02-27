import http.client


http_connection = http.client.HTTPConnection('news.fullerton.edu')
http_connection.request("GET", "/media/rankings.aspx")
resp = http_connection.getresponse()

if resp.reason == "OK":
    data = resp.read()
    print(data.decode())

http_connection.close()
