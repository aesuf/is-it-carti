import pandas as pd
import numpy as np

data = pd.read_csv('../data/music.csv')
X = data[data.columns[:26]]
y = data['carti']

def get_x():
	return X

def get_y():
	return y
