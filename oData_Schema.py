import http.client

conn = http.client.HTTPSConnection("services.odata.org")
payload = ''
headers = {}
conn.request("GET", "/V4/TripPinService/$metadata", payload, headers)
res = conn.getresponse()
data = res.read()
data = data.decode("utf-8")



# Ausgabe 
# Konsole
# print(data)

# Ausgabedatei
json_string = data
with open('json_odata_ablage.xml', 'w') as outfile:
    outfile.write(json_string)