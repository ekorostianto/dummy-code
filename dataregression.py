import pandas as pd
import numpy as np
import matplotlib.pylab as plt

a = np.arange(1, 11)
b = np.flip(a)
x = np.around([np.random.uniform(-0.1, 0.1, size=40)], decimals=4)

x1 = x[:,0:10].reshape(-1)
x2 = x[:,10:20].reshape(-1)
x3 = x[:,20:30].reshape(-1)
x4 = x[:,30:40].reshape(-1)

ax1 = a+x1
ax2 = b+x2
bx1 = a+x3
bx2 = b+x4


df = pd.DataFrame({
    'awal1': [ax1], 'awal2': [ax2], 'akhir1': [bx1], 'akhir2': [bx2]
}).to_csv(r'E:\KP_2020\Progress\regresi\datatest.csv')
