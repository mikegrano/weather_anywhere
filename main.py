import http.client
import json

def getweather():

    #Takes cli input on location and call type (forecast type)
    location = input("Which city do you want the forecast for? Use format <London,uk>")
    location = location.replace(',','%2C',1)
    timeframe = input("Which type of forecast ? Actual <a>, 5 Day <5d> or 10 Day <10d> ?  ")

    #Input validation
    if timeframe == "a" or timeframe == "5d" or timeframe == "10d":
        pass
    else:
        print("Not an option")
        exit(0)
    #print location selection
    print(location)

    '''Connection API call'''
    conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "xxxxxx"
        }

    #API connection strings passed to connection request
    connstring_actual = "/weather?units=metric&q="+location
    connstring_forecast5 = "/forecast?units=metric&q="+location
    connstring_forecast10 = "/forecast/daily?cnt=10&units=metric&q="+location

    if timeframe == "a":
        conn.request("GET", connstring_actual, headers=headers)
    elif timeframe == "5d":
        conn.request("GET", connstring_forecast5, headers=headers)
    elif timeframe == "10d":
        conn.request("GET", connstring_forecast10, headers=headers)

    res = conn.getresponse()
    datar = res.read()

    #Decode, parse json, print to screen
    decodedata = str(datar.decode('utf-8'))

    jsondata = json.loads(decodedata)
    for k, v in jsondata.items():
        print(k, v)

if __name__ == '__main__':
  getweather()
