# Quinten Rivers
### Log
###### Friday, November 16th, 2018
Trained a perceptron model to predict whether or not a song was created by Playboi Carti. Found out that a perceptron model was ~~a failure~~ highly unsuccessful. Might have to change parameters to get more success. Will try to include more `carti=True` songs in the training set.

UPDATE:
Changing to `test_size=0.25` was more accurate than `test_size=0.3`
### Models
#### Perceptron
```python
model=Perceptron()
test_train_split(X,y,test_size=0.3,random_state=4)
model.fit(X_train,y_train)
```
|n=116      |Predicted: NO|Predicted: YES|
|-----------|:-----------:|-------------:|
|Actual: NO |0            |111           |
|Actual: YES|0            |5             |

Saved as `$ROOT/QR/models/perceptron.joblib`
```python
model=Perceptron()
test_train_split(X,y,test_size=0.25,random_state=4)
model.fit(X_train,y_train)
```
|n=116      |Predicted: NO|Predicted: YES|
|-----------|:-----------:|:------------:|
|Actual: NO |81           |12            |
|Actual: YES|0            |4             |

Saved as `$ROOT/QR/models/perceptron_1.joblib`
