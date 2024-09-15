# -*- coding: utf-8 -*-
"""
Created on Mon May  1 15:49:01 2023

@author: Pau
"""
import matplotlib.pyplot as plt
import csv
first_element = []
fifth_element = []

csv_path=
with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    for id_row, row in enumerate(reader):
        if id_row == 0:
            continue
            first_element.append(row[0])     
            fifth_element.append(row[4])
        print(f"Date : {first_element}, Precipitation: {fifth_element} mm id_row: {id_row}")
        
    plt.figure(figsize=(35, 10))#horizontal and vertical dimensions
    plt.plot(first_element,fifth_element)
    #plt.pcolormesh(first_element,y_label,fifth_element)    
    plt.title('Rainfall in Emden Port ')
    plt.xticks(rotation=90)
    plt.ylabel('Precipitation [mm]')
    plt.xlabel('Date')
