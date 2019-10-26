import http.client
import json

def apicall():

    location = input("Which city do you want the forecast for? Use format <London,uk>")
    location = location.replace(',','%2C',1)
    print(location)

    conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "xxxxxxxxxxx"
        }
    connstring = "/weather?callback=test&id=2172797&units=metric&q="+location
    conn.request("GET", connstring, headers=headers)

    res = conn.getresponse()
    datar = res.read()

    decodedata = str(datar.decode('utf-8'))
    parsingdata = decodedata[5:-1]

    jsondata = json.loads(parsingdata)
    for k, v in jsondata.items():
        print(k, v)

if __name__ == '__main__':
  apicall()
