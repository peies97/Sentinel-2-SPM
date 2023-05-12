# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 22:50:27 2023

@author: Pau
"""
import json
from geopy import Point
from geopy.distance import distance
import numpy as np

def calculate_distance(geojson_path):
    cords=[]
    # Load your GeoJSON file
    with open(geojson_path) as f:
        data = json.load(f)
        
        # Extract the coordinates from the LineString geometry
        coordinates = data['features'][0]['geometry']['coordinates']
        cords = np.array(coordinates)
                
        # Calculate the distance between each coordinate
        distances = [0]
        start_point = Point(coordinates[0][1], coordinates[0][0]) #Point(latitude, longitude)
        for i in range(1, len(coordinates)):
            end_point = Point(coordinates[i][1], coordinates[i][0])
            dist = distance(Point(start_point), Point(end_point)).meters
            distances.append(dist)
            start_point = end_point
            
            #obtain a list with the absolute distance between the first coordinate and each coordinate
            absolute_distance = [distances[0]]
            running_total = distances[0]
            for i in range(1, len(distances)):
                running_total += distances[i]
                absolute_distance.append(running_total)            
    return(absolute_distance)
                
                
                
                
        