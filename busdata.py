import urllib.request
import sys
import time

import urllib.request
import sys
import time

sleep = 5 # 5 sec interval (be careful with this, we don't want to over load the API)
timespan =3600 # one hour(this can be edited)
end = time.time() + timespan
i = 0  

import urllib.request, json 
with open("busdata2.json", "w") as myfile:
    url = urllib.request.urlopen("http://data.itsfactory.fi/journeys/api/1/vehicle-activity")
    while time.time() < end:
        i += 1
        data = json.loads(url.read().decode("utf-8"))
        json.dump(data,myfile,indent=1)
        time.sleep(sleep)
        print(data)   
