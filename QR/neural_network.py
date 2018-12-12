import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import data
from sklearn.cross_validation import train_test_split

X = data.get_x()
y = data.get_y()
X_train,y_train,X_test,y_test = train_test_split(X,y,test_size=0.25)
model = Sequential()

model.add(Dense(activation='relu',
					input_dim=26,
					units=13,
					kernel_initializer='uniform'))

model.add(Dense(activation='relu',
					units=6,
					kernel_initializer='uniform'))

model.add(Dense(activation='sigmoid',
					units=26,
					kernel_initializer='uniform'))

model.compile(optimizer='adam',
							loss='binary_crossentropy',
							metrics=['accuracy'])

model.fit(X_train.values,y_train.values,batch_size=10,epochs=5)
