# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 02:51:25 2023

@author: Pau
"""
import os
def authenticate(path_code): 
    """TO READ USER AND PASSWORD FROM A .txt FILE LOCATED IN THE Path_Code""" 
    with open(os.path.join(path_code,'credentials.txt'), 'r') as f:
        user = f.readline().rstrip()
        password = f.readline()
    return user, password
