import http.client
import json

conn = http.client.HTTPSConnection("services.odata.org")
payload = json.dumps({
  "UserName": "maxmustermann",
  "FirstName": "Max",
  "LastName": "Mustermann",
  "Emails": [
    "MaxMustermann@web.de"
  ],
  "AddressInfo": [
    {
      "Address": "Dammstraße 1",
      "City": {
        "Name": "Heilbronn",
        "CountryRegion": "Deutschland",
        "Region": "ID"
      }
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/TripPinRESTierService/(S(wfosoe1agrmphpx05u113cct))/People", payload, headers)
res = conn.getresponse()
data = res.read()
data = data.decode("utf-8")




# Ausgabe 
# Konsole
# print(data)

# Ausgabedatei
json_string = data
with open('json_odata_ablage.json', 'w') as outfile:
    outfile.write(json_string)