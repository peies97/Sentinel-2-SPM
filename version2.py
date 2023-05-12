#!/usr/bin/env python3
# coding: utf-8
"""
Created on Sat Mar 11 01:43:42 2023

@author: Pau
"""
import SciHubDownload as shd
import extract as ex
import correct_safe_ac_ship as co
import authenticator as auth
import argsParse as ap
import sortFiles as sf
import netCDF as ncdf


def main():
    UTM_zoneNumber=32 #EMDEN, HAMBURG:32, BCN: 31
    UTM_zoneLetters='ULE' #EMDEN:ULE, BCN: TDF , HAMBURG: UNE
    cloudCover=20
    path_geojsons= r"C:\Users\pauta\Desktop\Thesis\Code\GEOJSONS\EMDEN" #CHANGE DEPENDING THE AREA
    path_code= r"C:\Users\pauta\Desktop\Thesis\Code"
   
    args = ap.parse_options()
    #Authenticate
    user,password = auth.authenticate(path_code)    
    #Download Sentinel-2  
    shd.downloader(user, password, args, UTM_zoneNumber, UTM_zoneLetters, cloudCover)    
    #Extract Zip
    ex.extractZip(args, path_code)    
    #Run Acolite
    co.run_acolite(args, path_code, path_geojsons)
    #Process the netCDF file
    sf.sortFiles(path_code,args)#check this
    
if __name__ == '__main__':
        main()