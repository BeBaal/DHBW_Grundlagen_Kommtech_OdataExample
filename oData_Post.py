import http.client
import json

conn = http.client.HTTPSConnection("services.odata.org")
payload = json.dumps({
  "UserName": "maxmustermann",
  "FirstName": "Max",
  "LastName": "Mustermann",
  "Gender": "Male"
})
headers = {
  'Content-Type': 'application/json'
}

# Individual key 'wfosoe1agrmphpx05u113cct'
# You can generate a key via https://services.odata.org/TripPinRESTierService

conn.request("POST", "/V4/TripPinService/(S(wfosoe1agrmphpx05u113cct))/People", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))