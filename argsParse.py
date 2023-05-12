# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 02:01:12 2023

@author: Pau
"""
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

def parse_options():
    __updated__ = '2023-01-23'
    __version__ = 0.1
    usage_text = '''
    %prog [options] Takes the input folder with safe files (as zip files)
    and correct them with acolite
    prog_name is '''
    
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (
        program_version, program_build_date)
    
    # Setup argument parser
    parser = ArgumentParser(
        description=usage_text, formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('--input',default='IN', help="The input folder where downloaded data will be stored ")
    parser.add_argument('--output',default='OUT', help='''The output folder where the corrected deata will be stored''')
    parser.add_argument('--start',default= '01012018', help='''The start date: ddmmyyyy [Default: f"{default} ]''')
    parser.add_argument('--end',default='31122018', help='''The end date: ddmmyyyy [Default: f"{default} ]''')
    parser.add_argument(
        '-V', '--version', action='version', version=program_version_message)
    #parser.add_argument("-v", "--verbose", dest="verbose", default=0,
     					#action="count", help="set verbosity level [default: %(default)s]")
                         
    # Process arguments
    args = parser.parse_args()
    print(args)
    return args