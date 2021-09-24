import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import tensorflow as tf
from keras.models import Model, Sequential
from keras.layers import Input, Activation, Dense
from keras.optimizers import SGD

data = pd.read_csv('E:/KP_2020/Progress/regresi/datatest.csv',',',
                  usecols=['awal1','awal2','akhir1', 'akhir2'])
A = data[['awal1','awal2','akhir1', 'akhir2']]
matrix = np.array(A.values,'float')

a = np.arange(1, 11)
b = np.flip(a)
X = np.concatenate((a, b, a, b), axis=0)

y1 = matrix[:,0]
y2 = matrix[:,1]
y3 = matrix[:,2]
y4 = matrix[:,3]

Y = np.concatenate((y1, y2, y3, y4), axis=0)

train_x = X
train_y = Y
# Create Network
inputs = Input(shape=(1,))
h_layer = Dense(8, activation='relu')(inputs)
h_layer = Dense(4, activation='relu')(h_layer)
outputs = Dense(1, activation='linear')(h_layer)
model = Model(inputs=inputs, outputs=outputs)

# Optimizer / Update Rule
sgd = SGD(lr=0.001)
# Compile the model with Mean Squared Error Loss
model.compile(optimizer=sgd, loss='mse')

# Train the network and save the weights after training
model.fit(train_x, train_y, batch_size=40, epochs=1000, verbose=1)
model.save_weights('weights.h5')

# Predict training data
predict = model.predict(np.array([26]))
print('f(26) = ', predict)

predict_y = model.predict(train_x)

# Draw target vs prediction
plt.plot(train_x, train_y, ‘r')
	plt.plot(train_x, predict_y, 'b')
plt.show()