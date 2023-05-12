# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 19:33:12 2023

@author: Pau
"""
import os
import shutil
from datetime import datetime
import argsParse as ap
path=r"C:\Users\pauta\Desktop\Thesis\Code"
args=ap.parse_options()
def sortFiles(path,args):
    # set the path to the directory containing the files
    dir_path=os.path.join(path, 'OUT_EMDEN')
    print(dir_path)
    # get a list of all files in the directory
    files = os.listdir(dir_path)

    # sort the files by their date
    files.sort(key=lambda x: datetime.strptime(x[11:19], '%Y%m%d'))
    
    # create a new list of sorted file paths
    sorted_files = [os.path.join(dir_path, file) for file in files]

    # move the files to a new directory in sorted order
    for i, file in enumerate(sorted_files):
        new_file = os.path.join(dir_path, f'{i+1:03d}_{os.path.basename(file)}')
        shutil.move(file, new_file)
        #os.remove(file)
        
    # print the sorted list of files
    print(files)
    return(files)

if __name__ == '__main__':
    sortFiles()


