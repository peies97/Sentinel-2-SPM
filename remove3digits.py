# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:31:30 2023

@author: Pau
"""
import os

# specify the directory path
directory = path_code= r"C:\Users\pauta\Desktop\Thesis\Code\OUT_EMDEN"

# loop through each folder inside the directory
for folder_name in os.listdir(directory):
    # check if the item is a directory and its name has at least 3 characters
    if os.path.isdir(os.path.join(directory, folder_name)) and len(folder_name) >= 4 and folder_name[0]=='0' or folder_name[0]=='1' :
        # remove the first 3 characters from the folder name
        new_folder_name = folder_name[4:]
        # create the new path for the renamed folder
        new_folder_path = os.path.join(directory, new_folder_name)
        # rename the folder
        os.rename(os.path.join(directory, folder_name), new_folder_path)
