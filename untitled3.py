# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:14:56 2021

@author: r140e
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
data = pd.read_csv(r'D:\College\Semester8\data\analisa\zonal_statistics\GWSFinal.csv', sep=';')
a = np.array(data)
ewh=a.reshape(11,12)
tahun=np.arange(2005, 2016)
#ewh = a[:,1:13]
#month = a[:,0].astype(int)
y_axis_labels = np.transpose(tahun) # labels for x-axis
x_axis_labels = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'] # labels for y-axis
plt.title("Perubahan GWS GLDAS 2005-2015 \n Basin Bengawan Solo dan Brantas")
plt.title("Perubahan GWS GLDAS 2005-2015 \n Basin Bengawan Solo dan Brantas")
sns.heatmap(ewh, linewidths=.5, cmap=("viridis"), xticklabels=x_axis_labels, yticklabels=y_axis_labels, annot=False)
plt.savefig(r'D:\College\Semester8\yudisium\raw data dan produk\Output\GWS GLDAS.png', dpi=300, bbox_inches='tight')

