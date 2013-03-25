'''
Description:     This scripts shows how you can geocode a CSV file containing customer addresses
                 to a point feature class using the ArcGIS Online geocoding service and the
                 Geocode Addresses geoprocessing tool.
Prerequisites:   To run the script you need to provide a valid username and password from your
                 ArcGIS Online Organization. Update the username and password variables in the
                 script before running it.
Service Credits: By default, the script will geocode the customers.csv provided in the input
                 folder. This CSV file has 10 records and so executing the script will deduct
                 10 * 80 / 1000 = 0.8 credits from your organization. 

'''

#Import modules
import arcpy
import sys
import os

#Get the folder contain the script to build paths relative to this folder
cwd = sys.path[0]

#Set Input and Output
input_table = os.path.join(cwd, "customers.csv")
#Create a file geodatabase to store the output feature class
output_gdb_name = "Outputs.gdb"
output_gdb = os.path.join(cwd, output_gdb_name)
if not os.path.exists(output_gdb):
    arcpy.management.CreateFileGDB(cwd, output_gdb_name)
output_feature_class = os.path.join(output_gdb,"CustomerLocations")

#Overwrite the output feature class if it already exists
arcpy.env.overwriteOutput = True

#Create the ArcGIS Server connection file
server_url = "https://geocode.arcgis.com/arcgis/services"
conn_file_name = "arcgis_online_batch_geocoding.ags"
conn_file = os.path.join(cwd, conn_file_name)
username = "<your username>"
password = "<your password>"
arcpy.mapping.CreateGISServerConnectionFile("USE_GIS_SERVICES", cwd, conn_file_name, server_url,
                                            "ARCGIS_SERVER", username=username, password=password)

#Build field mappings from the input table
input_mappings = {"Address": "Address",
                  "City":"City",
                  "Region" : "State",
                  "Postal" : "Zip"
                  }
field_mappings = arcpy.FieldInfo()
for field in input_mappings:
    field_mappings.addField(field, input_mappings[field], "VISIBLE", "NONE")

#Perform batch geocoding
address_locator = os.path.join(conn_file, "World.GeocodeServer")
arcpy.geocoding.GeocodeAddresses(input_table, address_locator, field_mappings,
                                 output_feature_class)
print arcpy.GetMessages()
