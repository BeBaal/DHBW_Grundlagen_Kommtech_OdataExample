import http.client

conn = http.client.HTTPSConnection("services.odata.org")
payload = ''
headers = {}
conn.request("GET", "/V4/TripPinService/(S(wfosoe1agrmphpx05u113cct))/People('maxmustermann')", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))