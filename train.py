import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout ,Activation, Flatten ,Conv2D, MaxPooling2D
import pickle


DATADIR = "img"
import os
CATEGORIES = len(os.listdir(DATADIR))+1


X = pickle.load(open("X.pickle",'rb'))
y = pickle.load(open("y.pickle",'rb'))

X = X/255.0

model = Sequential()
model.add(Conv2D(64,(3,3),input_shape = X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))


model.add(Conv2D(64,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))

model.add(Dense(CATEGORIES))
model.add(Activation('sigmoid'))

model.compile(loss="sparse_categorical_crossentropy",
				optimizer="adam",
				metrics=['accuracy'])

model.fit(X,y,batch_size=32,epochs=3,validation_split=0.2)

print(metrics['accuracy'])
model.save('SV.model')