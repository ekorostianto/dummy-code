# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 22:55:20 2021

@author: r140e
"""

"""
Created on Tue Jun 15 22:14:56 2021

@author: r140e
"""
import matplotlib.patches as mpatches
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from matplotlib.lines import Line2D
plt.style.use('ggplot')
data = pd.read_csv(r'D:\College\Semester8\data\analisa\zonal_statistics\indekskekeringan.csv', sep=';')
a = np.array(data)
ewh=a.reshape(11,12)
tahun=np.arange(2005, 2016)
#ewh = a[:,1:13]
#month = a[:,0].astype(int)
y_axis_labels = np.transpose(tahun) # labels for x-axis
x_axis_labels = ['Januari','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember'] # labels for y-axis
#plt.title("Anomali Groundwater Storage GLDAS 2005-2015 \n Basin Bengawan Solo dan Brantas")
#plt.title("Indeks Kekeringan GGDI 2005-2015 \n Basin Bengawan Solo dan Brantas")
cmap = plt.cm.bwr_r
norm = mpl.colors.Normalize(vmin=1, vmax=9)
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=10),
                Line2D([0], [0], color=cmap(.33), lw=10),
                Line2D([0], [0], color=cmap(.66), lw=10),
                Line2D([0], [0], color=cmap(1.), lw=10),
                Line2D([0], [0], color=('Black'), lw=10)
                ]
fig, ax = plt.subplots()
ax.set_title('Indeks Kekeringan GGDI 2005-2015 \n Basin Bengawan Solo dan Brantas')
#ax.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap))
#ax.legend(custom_lines, ['Tidak ada kekeringan', 'Kekeringan Ringan', 'Kekeringan Sedang', 'Kekeringan Tinggi', 'Kekeringan Ekstrim'], facecolor='white', edgecolor='white', loc="center", bbox_to_anchor=(0.45, -0.5))
sns.heatmap(ewh, linewidths=.5, cmap=("Oranges"), xticklabels=x_axis_labels, yticklabels=y_axis_labels)
plt.savefig(r'D:\College\Semester8\Laporan_TugasAkhir\gambar\IndexGGDI.png', dpi=300, bbox_inches='tight')

