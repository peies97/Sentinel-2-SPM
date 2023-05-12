#!/usr/bin/env python3
# coding: utf-8

import time
import glob
import sys
import os  # noqa
import acolite as ac  # noqa



__updated__ = '2023-01-23'
__version__ = 0.1


#args = ap.parse_options()

def run_acolite(args,path_code,path_geojsons):
    acolite_path=os.path.join(path_code,'acolite_py_win')
    sys.path.append(acolite_path)  #conda  noqa
    start_time=time.time()
    """Main function"""    
    poly = find_geojson(path_geojsons)
    files = glob.glob(os.path.join(args.input, '*.SAFE')) #args.input instead of inputFolder
    
    for f in files:
        FinalOutputPath=outputFolder(f,path_code,args.output)
        settings = {
            'inputfile': f,
            'polygon': poly,
            'output':  FinalOutputPath,
            'l2w_parameters': ['rhow_*', 'Rrs_*', 'spm_nechad2016', 'tur_nechad2016'],
            'rgb_rhot': True,
            'rgb_rhow': True,
            'rgb_rhos': True,
            'map_l2w': True,
            's2_target_res': 10,
            'l2w_mask': False
            
        }
        #if args.input:
         #  settings['limit'] = args.limit
         
        ac.acolite.acolite_run(settings=settings)
        print("Finished Processing")
        correct_time=time.time()-start_time
        print("Time to correct data: " + str(correct_time))

def find_geojson(path_geojsons):
    file_list = os.listdir(path_geojsons)
    # Search for a file with a .geojson extension
    for file_name in file_list:
        if file_name.endswith('Collection.geojson'):
            file_path = os.path.join(path_geojsons, file_name)
            break
    return file_path

    
def outputFolder(f,path_code,argument):
        f=f.replace('IN',"")
        f=f.replace('.SAFE',"")
        outputF=os.path.join(path_code,argument)
        outputPath= outputF + f;
        return outputPath
                            
if __name__ == '__main__':
    run_acolite()
