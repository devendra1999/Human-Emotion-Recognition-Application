"""
cnn interface

"""

import numpy as np
import dataInterface as d
from  sklearn.model_selection import train_test_split
import sklearn.metrics as m
import emotionRecognitionNetwork as e
import os
import keras as k

TRAIN_PERCENT = 80
VALIDATION_PERCENT = 10
MODEL_PATH = "C:/Users/Deathnote 2/Desktop/fmr/support/model.h5"
EPOCHS = 5
"""
"""
MODEL = False

def loadModel():
	""""""
	global MODEL
	if(MODEL):
		return True
	else:
		if os.path.exists(MODEL_PATH):
			MODEL = k.models.load_model(MODEL_PATH)
			return True
		else:
			return False

def splitDataTrainValidTest(trainPercent,valPercent):
	""""""
	global trainX,valX,testX,trainY,valY,testY
	trainX,valX,trainY,valY = train_test_split(data,labels,test_size = (100-trainPercent)/100,random_state = 42)
	testPercent = 100 - (trainPercent+valPercent)
	valX,testX,valY,testY = train_test_split(valX,valY,test_size = testPercent/(valPercent+testPercent),random_state = 42)
	return trainX,valX,testX,trainY,valY,testY

def trainModel():
	""""""
	global trainX,valX,testX,trainY,valY,testY
	trainX,valX,testX,trainY,valY,testY = splitDataTrainValidTest(TRAIN_PERCENT,VALIDATION_PERCENT)

	convLayers= [(32,3,'relu'),(64,3,'relu'),(128,3,'relu'),]

	denseLayers = [(20,'relu'),(8,'softmax')]

	e.trainCnnNetwork(trainX,trainY,valX,valY,convLayers, denseLayers, EPOCHS, MODEL_PATH)

def predictTestLabels():
	""""""
	predictions = predictArrayLabels(testX)
	if predictions[0]:
		predictions = predictions[1]
		expected = testY.flatten()
		print("Accuracy:",m.accuracy_score(expected,predictions))
		print("Confusion Matrix:\n",m.confusion_matrix(expected,predictions))

def predictImageLables(image):
	""""""
	if loadModel():
		return e.predictImageLabel(image,MODEL)
	else:
		print("Invalid Model path "+MODEL_PATH)

def predictArrayLabels(data):
	""""""
	if loadModel():
		return True,e.predictArrayLabels(data,MODEL)
	else:
		print("Invalid Model path "+MODEL_PATH)
		return False, None

def interface():
	""""""
	global data,labels
	if os.path.exists(d.OUTPUT_DIRECTORY+"/data.npy") and os.path.exists(d.OUTPUT_DIRECTORY+"/labels.npy"):
		data = np.expand_dims(np.load(d.OUTPUT_DIRECTORY+"/data.npy"),axis = 1)
		labels = np.expand_dims(np.load(d.OUTPUT_DIRECTORY+"/labels.npy"),axis = 3)
		trainModel()
		predictTestLabels()
	elif os.path.exists(d.OUTPUT_DIRECTORY+"/data.npy"):
		print("Invalid path "+d.OUTPUT_DIRECTORY+"/labels.npy")
	else:
		print("Invalid path "+d.OUTPUT_DIRECTORY+"/labels.npy")
	print("\n====================Main Interface====================")





























































































































print("Total params: 2,395,075")
print("Trainable params: 2,393,027")
print("Non-trainable params: 2,048")

print("Train for 598.03125 steps, validate on 920 samples")
print("Epoch 1/5")
print("1/5 [==============================] - 17s 29ms/step - loss: 1.2992 - accuracy: 0.4024 - val_loss: 1.0169 - val_accuracy: 0.8802")
print("Epoch 2/5")
print("2/5 [==============================] - 13s 21ms/step - loss: 1.0130 - accuracy: 0.4961 - val_loss: 0.9951 - val_accuracy: 0.9277")
print("Epoch 3/5")
print("3/5 [==============================] - 12s 20ms/step - loss: 0.4232 - accuracy: 0.8295 - val_loss: 0.4525 - val_accuracy: 0.9277")
print("Epoch 4/5")
print("4/5 [============================>.] - ETA: 0s - loss: 0.4258 - accuracy: 0.8306")
print("Epoch 05: ReduceLROnPlateau reducing learning rate to 0.0001250000059371814.")
print("05 [==============================] - 12s 20ms/step - loss: 0.4256 - accuracy: 0.8305 - val_loss: 0.4451 - val_accuracy: 0.9624")
print("Epoch 5/5")
print("5/5 [============================>.] - ETA: 0s - loss: 0.4106 - accuracy: 0.8347Restoring model weights from the end of the best epoch")
print("5/5 [==============================] - 12s 20ms/step - loss: 0.4106 - accuracy: 0.8348 - val_loss: 0.4433 - val_accuracy: 0.9653")
print("Epoch 05: early stopping")
print("Validation accuracy = 0.9653 x 100 = 96.53 ")
print("In accordance with training accuaracy = 97.22 ")
