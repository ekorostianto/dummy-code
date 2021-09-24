from pyhdf import SD
import numpy as np
import pandas as pd
from glob import iglob
import os
import sys

#make list hdf in folder to txt. remove ''' to uncoment
product_path = "/media/r140e/0AB80A130AB80A13/KP_2020/data/modis/myd11_l2"
input_files = pd.DataFrame(sorted(list(iglob(os.path.join(product_path, '**', '*.hdf'), recursive=True))))
with open('/media/r140e/0AB80A130AB80A13/KP_2020/data/modis/myd11_l2/myd11_l2.txt', 'w') as f:
    f.write(
        input_files.to_string(header = False, index= False)
    )

try:
	fileList=open('/media/r140e/0AB80A130AB80A13/KP_2020/data/modis/myd11_l2/myd11_l2.txt','r')
except:
	print('Did not find a text file containing file names (perhaps name does not match)')
	sys.exit()

#loops through all files listed in the text file
for FILE_NAME in fileList:
	FILE_NAME=FILE_NAME.strip()
	if 'L2' in FILE_NAME:#Same as above but for 10km MODIS file
		userInput=int(1)
		dataFields=dict([(1,'LST')])
	SDS_NAME=dataFields[int(userInput)] # The name of the sds to read
	try:
		# open the hdf file for reading
		hdf=SD.SD(FILE_NAME)
	except:
		print('Unable to open file: \n' + FILE_NAME + '\n Skipping...')
		continue
	
	# Get lat and lon info
	lat = hdf.select('Latitude')
	latitude = lat[:,:]
	min_lat=latitude.min()
	max_lat=latitude.max()
	lon = hdf.select('Longitude')
	longitude = lon[:,:]
	min_lon=longitude.min()
	max_lon=longitude.max()
	
	#get SDS, or exit program if SDS is not in the file
	try:
		sds=hdf.select(SDS_NAME)
	except:
		print('Sorry, your MODIS hdf file does not contain the SDS:',SDS_NAME,'. Please try again with the correct file type.')
		continue
	#get scale factor and fill value for data field
	attributes=sds.attributes()
	scale_factor=attributes['scale_factor']
	fillvalue=attributes['_FillValue']
	
	#get SDS data
	data=sds.get()
    #input overlay point
    #suf7
	#user_lat=float(-7.327922)
	#user_lon=float(112.713241)
    #suf6
	user_lat=float(-7.313076)
	user_lon=float(112.785212)
	if (user_lat < min_lat or user_lat > max_lat) or (user_lon < min_lon or user_lon > max_lon):
		asede = 1 #this dummy code
		#print(os.path.basename(FILE_NAME),'    kosong',)
		continue
	else:

		#Continues to ask for lat and lon until the user enters valid values
		while user_lat < min_lat or user_lat > max_lat:
			print(FILE_NAME, ' The latitude you entered is out of range. The range of latitude in this file is: ',min_lat,' to ',max_lat, 'degrees')
		while user_lon < min_lon or user_lon > max_lon:
			print(FILE_NAME, 'The longitude you entered is out of range. The range of longitude in this file is: ',min_lon, ' to ',max_lon,' degrees')
			
		#calculation to find nearest point in data to entered location (haversine formula)
		R=100#radius of the earth in meters
		lat1=np.radians(user_lat)
		lat2=np.radians(latitude)
		delta_lat=np.radians(latitude-user_lat)
		delta_lon=np.radians(longitude-user_lon)
		a=(np.sin(delta_lat/2))*(np.sin(delta_lat/2))+(np.cos(lat1))*(np.cos(lat2))*(np.sin(delta_lon/2))*(np.sin(delta_lon/2))
		c=2*np.arctan2(np.sqrt(a),np.sqrt(1-a))
		d=R*c
		#gets (and then prints) the x,y location of the nearest point in data to entered location, accounting for no data values
		x,y=np.unravel_index(d.argmin(),d.shape)
		'''print('\nThe nearest pixel to your entered location is at: \nLatitude:',latitude[x,y],' Longitude:',longitude[x,y])'''
		valid_data = data[x,y]*scale_factor
		celcius=round(valid_data-273.153,2)
		if data[x,y]==fillvalue:
			asede = 1
			#print(os.path.basename(FILE_NAME),'    ',fillvalue)
		else:
			print(os.path.basename(FILE_NAME),'    ', valid_data, '    ', celcius)