# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 08:40:28 2021

@author: r140e
"""
import numpy as np
import pandas as pd
from glob import iglob
import os
import sys
from osgeo import gdal

#make list hdf in folder to txt. remove ''' to uncoment
product_path = r"D:\College\Semester8\data\grace\rl05gramatprocessing\csv"
input_files = pd.DataFrame(sorted(list(iglob(os.path.join(product_path, '*.csv'), recursive=True))))
with open(product_path+'\list.txt', 'w') as f:
    f.write(
        input_files.to_string(header = False, index= False)
    )
try:
	fileList=open(product_path+'\list.txt','r')
except:
	print('Did not find a text file containing file names (perhaps name does not match)')
	sys.exit()
for FILE_NAME in fileList:
    FILE_NAME=FILE_NAME.strip()
    gdal.Translate(FILE_NAME + ".tif", FILE_NAME)
    
