import pandas as pd
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.externals import joblib

data = pd.read_csv('data/music.csv')
X = data[data.columns[:26]]
y = data['carti']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=4)

model = Perceptron()
model.fit(X_train,y_train)
pred = model.predict(X_test)

joblib.dump(model, 'QR/models/perceptron.joblib')
