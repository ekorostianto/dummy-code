# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 17:06:40 2021

@author: r140e
"""

import rioxarray
import rasterio
from pyproj import CRS
import matplotlib
import matplotlib.pyplot as plt
import geopandas as gpd
from rasterio.plot import show
from rasterio.mask import mask
import matplotlib as mpl
from descartes import PolygonPatch
import numpy as np
import fiona

with fiona.open(r'D:\College\Semester8\data\das\batasbasin.geojson') as shapefile:
    shapes = [feature["geometry"] for feature in shapefile]
trend = rasterio.open(r"D:\College\Semester8\software\GRACE_Matlab_Toolbox-master\TrendEWH2005-2015.grd")
src3 = rioxarray.open_rasterio(r"D:\College\Semester8\data\analisa\grace_rl05\gracegrd_201501.csv.tif")
src4 = rasterio.open(r"D:\College\Semester8\data\analisa\grace_rl05\gracegrd_200501.csv.tif")
basin = gpd.read_file(r'D:\College\Semester8\data\das\batasbasin.geojson')
'''with rasterio.open(r"D:\College\Semester8\data\analisa\grace_rl05\gracegrd_201001.csv.tif") as src:
    out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
    out_meta = src.meta'''
patches = [PolygonPatch(feature) for feature in shapes]
masked, mask_transform = mask(dataset=src4,shapes=basin.geometry,crop=True)
z = np.array(masked)
xmin=110.443887733772953
xmax=112.9419304000000466
ymin=-8.3015411659999359
ymax=-6.8084135055540855
fig, ax = plt.subplots()
#im = rasterio.plot.show(masked, title='EWH Grace Januari 2005 (mm)', transform=(mask_transform))
#plt.colorbar([z[0]])
im = ax.add_collection(mpl.collections.PatchCollection(patches))

im = ax.imshow(z[0], extent=(xmin, xmax, ymin, ymax))
cax = fig.add_axes()
ax.set_title('Basin Bengawan Solo dan Brantas')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
fig.suptitle('Trend EWH Grace 2005-2015 (mm)', fontsize=16)
fig.colorbar(im, cax=cax, orientation='vertical')
plt.show()
'''#plt.colorbar()
#plt.show()
plt.style.use("ggplot")
plt.title("Trend EWH Grace 2005-2015 (mm)")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.ticklabel_format(style="plain")'''