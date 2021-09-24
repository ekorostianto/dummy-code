# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 04:18:23 2021

@author: r140e
"""
import fiona
import rasterio
import rasterio.plot
from rasterio.crs import CRS
import matplotlib.pyplot as plt
import matplotlib as mpl
from descartes import PolygonPatch
import numpy as np
from rasterio.plot import show
from matplotlib import collections as cplt
import rasterio.mask
import scipy.io


with fiona.open(r"D:\College\Semester8\data\das\batasbasin.shp", "r") as shapefile:
    features = [feature["geometry"] for feature in shapefile]
grace = rasterio.open(r"D:\College\Semester8\data\grace\gracerl05\CSR_GRACE_RL05_Mascons_v01.nc")
gracemm = grace.read(31)*10
#gracemm.boundsBoundingBox(left=358485.0, bottom=4028985.0, right=590415.0, top=4265115.0)
'''
    out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
    out_meta = src.meta
out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform})
with rasterio.open("masked2.tif", "w", **out_meta) as dest:
    dest.write(out_image)
'''
#mat = scipy.io.loadmat(r"D:\College\Semester8\software\GRACE_Matlab_Toolbox-master\GRACE_results\gracegsm60_2005-2015_swensongia300km.mat")
src1 = rasterio.open(r"D:\College\Semester8\data\gldas\noah025_m_2_1\giovanni.gsfc.nasa.gov\Canop\tiff\masked\shapeMasked.scrubbed.GLDAS_NOAH025_M_2_1_CanopInt_inst.20050101.tif")
src2 = rasterio.open(r"D:\College\Semester8\data\analisa\grace_rl05\masked\gracegrd_200501.csv.tif")
src3 = rasterio.open(r"D:\College\Semester8\software\GRACE_Matlab_Toolbox-master\GSM_200501.grd")
src4 = rasterio.open(r"D:\College\Semester8\data\grace\gracerl05\CSR_GRACE_RL05_Mascons_v01.nc")
#x=mat.items()
#y=list(x)
#z=np.array(y)
#zz=z[4,::]
#zzz=zz[:,1]
#raster = rasterio.open(mat)
#r3 = src3.from_epsg(4326)#110.4438877337729537,-8.3015411659999359 : 112.9419304000000466,-6.8084135055540855
src3.BoundingBox(left=110.443887733772953, bottom=-8.3015411659999359, right=112.9419304000000466, top=-6.8084135055540855)
raster1 = src1.read(1)
raster2 = src2.read(1)
raster3 = src3.read(1)
raster4 = src4.read(141)
fig, ax = plt.subplots()
rasterio.plot.show((src3, 1), ax=ax)
patches = [PolygonPatch(feature, edgecolor="red", facecolor="none", linewidth=2) for feature in features]
ax.add_collection(cplt.PatchCollection(patches, match_original=True))
#ax.set_xlim(min_y, max_y)
#ax.set_ylim(min_x, max_x)
plt.colorbar()
plt.show()
#rasterio.plot.show((src2, 1))
#ax = mpl.pyplot.gca()
#patches = [PolygonPatch(feature, edgecolor="red", facecolor="none", linewidth=2) for feature in features]
#ax.add_collection(mpl.collections.PatchCollection(patches))
#raster4mm = raster4*10 #31, 91, 141
#D:\College\Semester8\software\GRACE_Matlab_Toolbox-master\GRACE_results\gracegsm60_2005-2015_swensongia300km.mat
#fig, (axa, axb, axc) = plt.subplots(1,3, figsize=(21,8))
#show(raster1, ax=axa, title='EWH Grace Januari 2005 (mm)')
#show(raster2, ax=axb, title='EWH Grace Januari 2010 (mm)')
#show(raster3, ax=axc, title='EWH Grace Januari 2015 (mm)')
#rasterio.plot.plotting_extent(src4[30], transform=None)
#plt.imshow((raster2))
#plt.colorbar()
#plt.title('EWH Grace Januari 2005 (mm)')
#plt.title('Canopy Plant Water Januari 2005 (cm)')
#plt.title('EWH Grace Mascon L3 Januari 2005 (mm)')
#plt.xlabel('Longitude')
#plt.ylabel('Latitude')
#plt.show()
