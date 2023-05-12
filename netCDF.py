# -*- coding: utf-8 -*-
"""
Created on Mon May  8 01:15:17 2023

@author: Pau
"""
import netCDF4 as nc
import os
import glob
import numpy as np
import json
import csv
import pyproj
import pandas as pd
import calculateDistance as cd
import matplotlib.pyplot as plt

# UTM Zone of Emden/Hamburg 32, BCN 31
UTM_zoneNumber = '32' #CHANGE THIS!

# Open the netCDF file
path_geojsons=r'C:\Users\pauta\Desktop\Thesis\Code\GEOJSONS\EMDEN\emden_boatPath4.geojson' #emdenTwoPoints.geojson or emden_boatPath4.geojson'
OUT_path=r'C:\Users\pauta\Desktop\Thesis\Code\OUT_EMDEN'
csv_path=r"C:\Users\pauta\Desktop\Thesis\Code\export.csv"
#path_geojsons=r'C:\Users\pauta\Desktop\Thesis\Code\GEOJSONS\EMDEN\emden_boatPath.geojson'
#OUT_path=r'C:\Users\pauta\Desktop\Thesis\Code\CorrectedData'
OUT_files = os.listdir(OUT_path) 
desired_attr_list = []

dist = np.array(cd.calculate_distance(path_geojsons)) #x-axis
spm_values_array= np.zeros((len(OUT_files), len(dist)))
time = []
first_element = []
fifth_element = []

#time=np.zeros(len(OUT_files)) #specify length

not_processed=0
show_globalAttributes=0
show_dimensions=0
show_variables=0
show_varAttributes=0
show_xy=0
plot_spmMap=0
plot_distanceTime=1
plot_Boatpath=0
plot_precipitation=0

def main():
    for i, f in enumerate (OUT_files):
            print('Processing file ',f)
            for g in f:
                desired_nc='*L2W.nc*'
                list_nc= glob.glob(OUT_path + '/' + f + '/'+ desired_nc)            
                nc_file= nc.Dataset(list_nc[0], 'r')
                
                #Get  dimensions, attributes and variables
                dimensions = nc_file.dimensions  #list of dimensions such as X and Y 
                global_attributes = nc_file.ncattrs() #global variables
                variables = nc_file.variables  # list of nc variables
       
            #Show dimensions
            if show_dimensions:             
                print ("\nNetCDF dimension information:")
                for dim in dimensions:
                    print("Name: ", dim)
                    print ("\t\tsize:", len(nc_file.dimensions[dim]))
                
            #Print Global attributes      
            if show_globalAttributes:                      
                print ("\n\nNetCDF Global Attributes:")            
                for attribute_name in global_attributes:
                    print(f"{attribute_name} :", nc_file.getncattr(attribute_name))
         
            #Print variables 
            if show_variables:        
                print ("\n\nNetCDF variable information:")
                for var in variables:
                    if var not in dimensions:
                        print ('\tName:', var)
                        print ("\t\tdimensions:", nc_file.variables[var].dimensions)
                        print ("\t\tsize:", nc_file.variables[var].size)
            
            #Access the desired variable        
            try:
                desired_var = nc_file.variables['SPM_Nechad2016_665']
            except Exception:
                desired_var = nc_file.variables['SPM_Nechad2016_665'] 
                     
            # Print the local attributes of the variable
            if show_varAttributes:    
                print("\n\n Attributes of the variable ", desired_var)
                
            # get the x and y coordinate values
            x_vals = nc_file.variables['x'][:]
            y_vals = nc_file.variables['y'][:]
            x_array = []
            y_array = []
            x_array.append(x_vals)
            y_array.append(y_vals)

            lats= nc_file.variables['lat'][:]
            lons= nc_file.variables['lon'][:]
        
            # Open the GeoJSON file
            with open(path_geojsons) as f:
                data = json.load(f)
           
            #Extract the date of the file
            time_value=nc_file.getncattr('isodate')[:10]
            time.append(str(time_value))         
            
            # Extract the latitude and longitude coordinates from the file
            coordinates = data['features'][0]['geometry']['coordinates'][:]
            lats_path = [coord[1] for coord in coordinates]
            lons_path = [coord[0] for coord in coordinates]
       
            # Define the projection you want to convert to
            project = pyproj.Proj(proj='utm', zone= UTM_zoneNumber, ellps='WGS84')

            # Convert the latitude and longitude coordinates to x and y meters
            x_path, y_path = project(lons_path, lats_path)

            # Print the results
            if show_xy:
                print('\nThese are the x values of the netCDF file: ', x_vals)
                print('\nThese are the y values of the netCDF file: ', y_vals)
                print('\nThis is the desired boat path X: ',x_path)
                print('\nThis is the desired boat path y: ',y_path)
        
            #get the x, y indices that contain the desired x,y values of the BOAT PATH
            x_index = []  
            y_index = []         
            for xx in x_path:
                distt = np.abs(np.array(x_vals) - xx)
                closest_index = np.argmin(distt)
                x_index.append(closest_index)   
              
            for yy in y_path:
                distt = np.abs(np.array(y_vals) - yy)
                closest_index = np.argmin(distt)
                y_index.append(closest_index)
            
            if show_xy:    
                print('\nIndices of x\n',x_index)
                print('\nIndices of y\n',y_index)      
        
            if plot_spmMap: #to plot a SPM map 
                spm_values = desired_var[:,:]
                spm_values = np.ma.masked_invalid(spm_values)
                plt.figure(figsize=(10, 8))
                plt.pcolormesh(lons, lats, spm_values)
                plt.colorbar()
                plt.xlabel('Longitude')
                plt.ylabel('Latitude')
                plt.title('Suspended Particulate Matter of day ' + time_value)
                plt.show() 
                
            if plot_distanceTime: #to plot a time/distance plot
                spm_values=[]
                for idx, y in enumerate(y_index):
                    spm_values.append(desired_var[y,x_index[idx]])
                spm_values=np.asarray(spm_values)
                #spm_values[np.isnan(spm_values)]=-1  
                spm_values_array[i,:]=spm_values                
             
    if plot_precipitation:
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)
            for id_row, row in enumerate(reader):
                if id_row == 0:
                    continue
                #if row[0] == time[i]:
                    first_element.append(row[0])     
                    fifth_element.append(row[4])
                    #print(f"Date : {first_element}, Precipitation: {fifth_element} mm id_row: {id_row}")
                        
            plt.figure(figsize=(35, 10))#horizontal and vertical dimensions
            plt.bar(first_element,fifth_element)
            #plt.pcolormesh(first_element,y_label,fifth_element)    
            plt.title('Snow in Emden Port ')
            plt.xticks(rotation=90)
            plt.ylabel('Snow [mm]')
            plt.xlabel('Date')
     
    #group data within month and compute the month average 
    time_array = np.array(time)
    date_index = pd.to_datetime(time_array)
    data = np.array(spm_values_array)
    df = pd.DataFrame(data, index=date_index)


    # create date range with monthly frequency
    all_months = pd.date_range(start='2018-01', end='2022-12', freq='MS').strftime('%Y-%m').values #NEED TO PARAMETRIZE THIS TO time_array
    all_months=pd.to_datetime(all_months)

    print('spm_values_array:\n', spm_values_array)
    print('Available months', time_array)

    # THIS IS TO PLOT ALSO ALL-NAN MONTHS ->need to include ALL month, eeven the ones with all-nan values
    monthly_average = df.groupby(pd.Grouper(freq='M')).apply(lambda x: x.mean(skipna=True))
    monthly_average_array = np.array(monthly_average)
    monthly_average_array[np.isnan(monthly_average_array)]=-1 
    print('\nmonths averages 1:\n', monthly_average_array)
    
    # Retrieve list of the UNIQUE averaged months
    months = np.array([idx.date().strftime('%Y-%m') for idx in all_months])
    unique_months, indices = np.unique(months, return_index=True)
    print('\nmonths averages RESULT:\n',   monthly_average_array)
    print('\nUNIQUE months averaged:\n', unique_months)

        
    normalized_arr = (monthly_average_array - np.min(monthly_average_array)) / (np.max(monthly_average_array) - np.min(monthly_average_array))
    plt.figure(figsize=(35, 15)) #horizontal and vertical dimensions
    plt.pcolormesh(unique_months,dist, np.transpose(normalized_arr))
    plt.colorbar()
    plt.title('SPM Value trace of a boat path in Emden Port')
    plt.xticks(rotation=90)
    plt.ylabel('Distance [m]')
    plt.xlabel('Date')
    plt.show()
      
    #Close the netCDF file        
    nc_file.close()         
    if plot_Boatpath:      
        #Plot boat path
        plt.figure(figsize=(10, 10))
        lats_path[::-1]
        lons_path[::-1]
        plt.plot(lons_path, dist)
        plt.xlabel('longitude')
        plt.ylabel('Distance from starting point')
        plt.title('Boat path')
        plt.show()
    

if __name__ == '__main__':
        main()