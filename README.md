# Bus-Data-Project

This is a Python program that records real time location data about the buses of the Tampere public transportation network. 
Such data can be retrieved easily from the Journeys API offered by ITS Factory.

The program receives three command line parameters:

  The name of the file into which it should store the information.
  The time interval (in seconds) between successive data retrievals from the Journeys API. E.g. if this parameter is 5, then new data is retrieved every 5 seconds.
  The time (in seconds) how long the program should keep recording the information. E.g. if this parameter is 3600, then the program will continue to retrieve and store the data for one hour. If the time interval specified by the preceding parameter would be 5, then this would mean that the program would retrieve roughly 3600/5 = 720 pieces of data during its execution. For example the command python busdata.py busdata.json 5 3600 would keep reading bus data every 5 seconds for one hour and store all received data as such into the file busdata.json.
Note: When you test this program, do not give a value smaller than 5 for the interval between successive data retrievals. 
We do not wish to cause unnecessary load to the Journeys API server. Retrieving data every 5 seconds is often enough for test purposes. 
The Journeys API is very simple to use: simply visiting the address http://data.itsfactory.fi/journeys/api/1/vehicle-activity returns information about all currently active buses within the Tampere public transportation network. The data is in JSON format. 

Once the data is stored in json format, we proceed to run simple analysis such as calculating bus delay time, average speed per trip and frequency.
