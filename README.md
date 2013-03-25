batch-geocoding-python
======================

This scripts shows how you can geocode a CSV file containing customer addresses to a point feature class using the ArcGIS Online geocoding service and the Geocode Addresses geoprocessing tool.

To run the script you need to provide a valid username and password from your
ArcGIS Online Organization. Update the username and password variables in the
script before running it.

By default, the script will geocode the customers.csv provided in the input
folder. This CSV file has 10 records and so executing the script will deduct
10 * 80 / 1000 = 0.8 credits from your organization. 
