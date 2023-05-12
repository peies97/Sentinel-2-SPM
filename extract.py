# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 02:56:40 2023

@author: Pau
"""
import zipfile
import os
import glob

def extractZip(args, path_code): 
    """TO EXTRACT .SAFE FILE FROM DOWNLOADED .zip"""
    files = glob.glob(os.path.join(args.input, '*.zip')) #args.input instead of inputFolder
    for f in files:
        #Unzip the downloaded .SAFEs
        zip_filename = os.path.join(path_code,f)   
        print('file to extract: ' + zip_filename)
        # Directory to extract files to
        inn= os.path.join("/", args.input)
        extract_dir = path_code + inn
        print("Extract directory " + extract_dir)
        # Create the directory if it doesn't exist
        if not os.path.exists(extract_dir):
            os.makedirs(extract_dir)
            
        # Open the ZIP file for reading
        with zipfile.ZipFile(zip_filename, "r") as zip_ref:
        # Extract all files to the directory
            zip_ref.extractall(extract_dir)
        os.remove(zip_filename)
        
   


