# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:17:30 2021

@author: r140e
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy
from scipy.interpolate import make_interp_spline


TWSgramat = pd.read_excel (open('D:/College/Semester8/data/analisa/zonal_statistics/twsgramat2005-2015fix.xlsx', 'rb'), sheet_name='bulanan')
a = np.array(pd.DataFrame(data=TWSgramat))
x=a[:,:1]
y=a[:,1:2]
#x_new = np.linspace(200501, 201507, 21)
#a_BSpline = scipy.interpolate.make_interp_spline(x, y)
#y_new = a_BSpline(x_new)
plt.plot(x,y)
plt.grid()
plt.suptitle('Grafik EWH Bulanan 2005-2015')
plt.title('Basin Bengawan Solo - Brantas (mm)')
plt.xlabel('Tahun')
plt.ylabel('EWH')
plt.show()