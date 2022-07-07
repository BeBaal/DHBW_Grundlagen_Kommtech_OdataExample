import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPSConnection("services.odata.org")
boundary = ''
payload = ''
headers = {
  'If-Match': 'W/"08DA601160CE1426"',
  'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
}
conn.request("DELETE", "/V4/TripPinService/People('maxmustermann')", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))