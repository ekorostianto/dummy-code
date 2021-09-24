from IPython import get_ipython
get_ipython().magic('reset -sf')
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.DataFrame([[0.000083,24.1],[0.000064,36.35],[0.00007,37.2],[0.00008,24.62],[0.000048,27.54],[0.00006,23.63],[0.000068,38.18],[0.000105,22.75],[0.000129,29.19],[0.000051,40.54],[0.00008,36.6],[0.000046,22.1],[0.00006,30.08],[0.000075,32.45],[0.00006,144.38],[0.000045,116.04],[0.000066,65.58],[0.000073,32.94],[0.000054,31.67],[0.000062,27.71],[0.000077,36.64],[0.000111,54.9]])
df.columns = ['x', 'y']
x_train = df['x'].values[:,np.newaxis]
y_train = df['y'].values
r2 = r2_score(y_train, x_train)
lm = LinearRegression()
lm.fit(x_train,y_train) #fase training
print('Coefficient : ' + str(lm.coef_))
print('Intercept : ' + str(lm.intercept_))
print(r2)
x_test = [[170],[171]] #data yang akan diprediksi
p = lm.predict(x_test) #fase prediksi
print(p) #hasil prediksi
#prepare plot
pb = lm.predict(x_train)
dfc = pd.DataFrame({'x': df['x'],'y':pb})
plt.scatter(df['x'],df['y'])
plt.plot(dfc['x'],dfc['y'],color='red',linewidth=1)
plt.xlabel('citra')
plt.ylabel('insitu')
plt.show()