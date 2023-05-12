## About version2
This script performs the following actions:

	*Downloads the batch of L1C Sentinel-2 data from Copernicus 
	 SciHub of the desired UTM zone and sensing dates in .zip files

	*Extracts the .SAFE folder of each downloaded .zip. Then the .zip files are removed
	
	*Runs Acolite software

	*Access to all the L2W.netCDF output files that result from the
	 Acolite software.

	*Plots the time-space SPM variation of the Emden Port
______________________________________________________________

Command-line: python version2.py --input IN --output OUT --start ddmmyyyy --end ddmmyyyy
______________________________________________________________

Note: The downloaded Sentinel-2 batch is stored inside a folder parsed 
	in the command line (or DEFAULT="IN"), located  in 'path_code'  
	(the same path as Acolite).

Note: The corrected data from Acolite output is stored inside a folder 
	parsed in the command line (or DEFAULT='OUT') located in 
	'path_code' (the same path as Acolite).

Note: to subnet the downloaded data with a polygon [RECOMENDED], a 
	.geojson with the desired polygon has to be added to the 
	path_code folder.

Note: A 'credentials.txt' file must be created in 'path_code' containing 
	ONLY a line with Copernicus SciHub User and a second line with
	password:
		user
		password

Note: Although it is specific for Emden Port, it can be adjusted to fit other areas
	but then it is required to change the UTM zone inside version2.py and provide
	the proper .geojson for bounding the region that ACOLITE will use and the 
	proper .geojson with the new port waterway coordinates of your interest.

*Recomendation: Create a new folder that will be the 'path_code' (e.g. in Desktop) 
		    and extract Acolite files inside it. Use Anaconda Navigator to
		    install the required libraries and modules and Anaconda prompt
		    to run the script.
		 
*Required Libraries and modules:
	acolite
	matplotlib	
	gdal
	glob
	numpy
	csv	
	sentinelsat
	zipfile
	netCDF4
	json
	pandas


