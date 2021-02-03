# Bus-Data-Project

#Part One busdata.py
This is a Python program that records real time location data about the buses of the Tampere public transportation network. 
Such data can be retrieved easily from the Journeys API offered by ITS Factory.

The program receives three parameters:

  a) The name of the file into which it should store the information.
 b)The time interval (in seconds) between successive data retrievals from the Journeys API. E.g. if this parameter is 5, then new data is retrieved every 5 seconds.
  c) The time (in seconds) how long the program should keep recording the information. E.g. if this parameter is 3600, then the program will continue to retrieve and store the data for one hour. If the time interval specified by the preceding parameter would be 5, then this would mean that the program would retrieve roughly 3600/5 = 720 pieces of data during its execution. For example th eparameters  busdata.json, 5, 3600 would keep reading bus data every 5 seconds for one hour and store all received data as such into the file busdata.json.
Note: When you test this program, do not give a value smaller than 5 for the interval between successive data retrievals. 
We do not wish to cause unnecessary load to the Journeys API server. Retrieving data every 5 seconds is often enough for test purposes. 
The Journeys API is very simple to use: simply visiting the address http://data.itsfactory.fi/journeys/api/1/vehicle-activity returns information about all currently active buses within the Tampere public transportation network. The data is in JSON format. 

#Part two bus busdatastats.py.

Once the data is stored in json format, we proceed to to calculate 
•	How many different vehicles appear in the data (for the particular bus line)?
•	How many unique data points were recorded (for the particular bus line)? 
Here "unique" means unique in terms of time and a particular vehicle: the data may contain several data points that correspond to the same time and the same vehicle. The information is printed in increasing order of the bus lines (in lexicographic ordering; produced). The information for each bus line X is printed on a single line in the form X: y vehicles and z data points, where y is the number of different vehicles and z the number of unique data points. 

The code relies on the fact that the bus data is formatted in an indented multiline format, where each line of form "}\n" or "}" marks the end of one complete top-level JSON dictionary.

#Part three busspeeds.py 

We continue to analyze the bus data recorded into busdata.json. Now the task is to draw a graph that shows the speed of some single bus (a unique vehicle) throughout the recorded data. The x-axis corresponds to the order of the data points in time, and the y-axis to the speed (km/h). The graph contains two line curves: one, that derives the speed directly from the 'speed' attributes given in the bus data, and one, that calculates the bus speed from the bus location coordinates and the time information. The graph hence may give us some assurance about the accuracy of the bus speed values given in the original bus data: if the two different lines coincide well with each other, the speed data may be deemed to be reliable.
To calculate speed values, Let data[i-1] and data[i] denote two successive (in terms of time) data points for a single bus. The average speed of the bus when it travels between the points can be calculated from the following two pieces of information:

