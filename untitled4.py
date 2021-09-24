# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 23:34:39 2021

@author: r140e
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
data = pd.read_csv(r'D:\College\Semester8\data\analisa\zonal_statistics\IndexGDSI.csv', sep=';',keep_default_na=True)
a = np.array(data)
ewh=a.reshape(11,12)
tahun=np.arange(2005, 2016)
#ewh = a[:,1:13]
#month = a[:,0].astype(int)
y_axis_labels = np.transpose(tahun) # labels for x-axis
x_axis_labels = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'] # labels for y-axis
#plt.title("Anomali Groundwater Storage GLDAS 2005-2015 \n Basin Bengawan Solo dan Brantas")
plt.title("Grace Drought Severity Index 2005-2015 \n Basin Bengawan Solo dan Brantas")
sns.heatmap(ewh, linewidths=.5, cmap='YlOrRd_r', xticklabels=x_axis_labels, yticklabels=y_axis_labels)
