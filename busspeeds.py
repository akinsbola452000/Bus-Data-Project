"""
Created on Wed Feb  3 14:18:16 2021

@author: BolarinwaAkindaini
"""
from math import radians, cos, sin, asin, sqrt
import matplotlib.pyplot as plt
from datetime import datetime
import io
import json
import numpy as np




def haversine(p1, p2):  # p1, p2 coordinate points of form [latitude, longitude]
    # convert decimal degrees to radians (also ensures values are floats) 
    pr1 = [radians(float(p1[0])), radians(float(p1[1]))]
    pr2 = [radians(float(p2[0])), radians(float(p2[1]))]

    # haversine formula
    dlat = pr2[0] - pr1[0]   # difference of latitudes
    dlon = pr2[1] - pr1[1]   # difference of longitudes
    a = sin(dlat/2)**2 + cos(pr1[0]) * cos(pr2[0]) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

route = "3" #specify bus route
vehicle = "TKL_42" # Specify bus 
speeds = []
locs = []
times = []
with open("busdata.json", 'r') as infile:
    databuf = io.StringIO()
    for line in infile:
        databuf.write(line)
        if line == '}\n':
            databuf.seek(0)
            data = json.load(databuf)
            databuf.close()
            databuf = io.StringIO()
            for trip in data['body']:
                bus = trip['monitoredVehicleJourney']
                if bus['lineRef'] == route:
                    if vehicle == None:
                        vehicle = bus['vehicleRef']
                    if vehicle == bus['vehicleRef']:
                        t = datetime.strptime(trip['recordedAtTime'],
                                              '%Y-%m-%dT%H:%M:%S.%f+03:00')
                        if len(times) == 0 or times[-1] != t:
                            speeds.append(float(bus['speed']))
                            locs.append([float(bus['vehicleLocation']['latitude']),
                                    float(bus['vehicleLocation']['longitude'])])
                            times.append(t)

speeds2 = []
for i in range(1, len(times)):
    duration = times[i] - times[i-1]
    sp = (haversine(locs[i-1], locs[i])/duration.total_seconds())*3600
    speeds2.append(sp)

plt.plot(speeds)
plt.plot(speeds2)
#plt.savefig(argv[2])
plt.show()
