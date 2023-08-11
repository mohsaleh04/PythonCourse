# 1 2 3 4 5 6 | 20
# 1 3 5 7 9 11 | ?

from tensorflow import *
import numpy as np
from keras import Sequential
from keras.layers import Dense

x = np.array([1, 40, 35, 28, 100, 72], dtype=float)
y = np.array([33.8, 104, 95, 82.4, 212, 161.6], dtype=float)

# print(x.shape) # (6,)

modelLayers = [
	Dense(units=1, input_shape=[1,]), # Input
	Dense(units=3), # Hidden Layer
	Dense(units=2), # Hidden Layer
	Dense(units=1) # Output
]

model = Sequential(modelLayers)
model.compile(optimizer=optimizers.Adam(0.1), loss=losses.MSE)
model.fit(x, y, epochs=250)

prediction = model.predict([0, 100, 50])
print(prediction)
