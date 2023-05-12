# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 23:11:33 2023

@author: Pau
"""
import time
from sentinelsat import SentinelAPI
import datetime
from collections import OrderedDict
 
def downloader(user, password, args, UTM_zoneNumber, UTM_zoneLetters,cloudCover) :  
    """TO DOWNLOAD DATA FROM SCI HUB""" 
    start_time=time.time()
    #login to SCIHUB
    api = SentinelAPI(user, password)

    #Sensing date
    start_year= int(args.start[-4:])
    start_month=int((args.start)[2:4])
    start_day=int((args.start)[:2])
    print('Start date: ' + str(start_year) + ', ' + str(start_month) + ', ' + str(start_day))
    
    end_year=int((args.end)[-4:])
    end_month=int((args.end)[2:4])
    end_day=int((args.end)[:2])
    print('End date: ' + str(end_year) + ', ' + str(end_month) + ', ' + str(end_day))
    
    print('Zone: ' + str(UTM_zoneNumber) + str(UTM_zoneLetters) )

    start_date = datetime.datetime(int(start_year), int(start_month), int(start_day),0,0)
    end_date = datetime.datetime(int(end_year), int(end_month), int(end_day),23,59,59)     
    zone= str(UTM_zoneNumber) + UTM_zoneLetters
    tiles = [zone]
    
    #Query
    query_kwargs = {
            'platformname': 'Sentinel-2',
            'producttype': 'S2MSI1C',
            'date': (start_date, end_date),
            'cloudcoverpercentage': (0,cloudCover)}
            

    products = OrderedDict()
    for tile in tiles:
        kw = query_kwargs.copy()
        kw['tileid'] = tile
        pp = api.query(**kw)
        products.update(pp)
        
    api.download_all(products,directory_path=args.input)
    print('Start date: ')
    print(start_date)
    print('End date: ')
    print(end_date)
    download_time=time.time()-start_time
    print("Time to download data: " + str(download_time))
    
if __name__ == '__main__':
    downloader()