

import numpy as np

from BackPropagationNN import NeuralNetwork

from sklearn import datasets
from sklearn import preprocessing
from sklearn import cross_validation
from sklearn import metrics
import csv

SIZE_OF_TRAIN = 68870
DIMESION_OF_INPUT = 28*28


def trainFileReader():
	print "reading training file.."
	with open('../input/trainPlus.csv', 'r') as trainFile :
		trainReader = csv.reader(trainFile, delimiter=',', quotechar='"')
		trainFile.next()

		trainData = np.zeros((SIZE_OF_TRAIN,DIMESION_OF_INPUT),dtype=float)
		trainTarget = np.zeros(SIZE_OF_TRAIN)
		j = 0
		print "recognize file data.."
		for valueOfIteration in xrange(SIZE_OF_TRAIN) :
			row = trainReader.next()
			matrix = np.zeros(DIMESION_OF_INPUT)
			trainTarget[j] = row[0]
			for i in range(DIMESION_OF_INPUT) :
				matrix[i] = row[i+1]

			trainData[valueOfIteration] = matrix
			j+=1
		print "recognize file data done.."
		return (trainData,trainTarget)



def targetToVector(x):
	# Vector
	a = np.zeros([len(x),10])
	for i in range(0,len(x)):
		a[i,int(x[i])] = 1
	return a

def main():

	# Digits dataset loading
	# digits = datasets.load_digits()
	X_raw, y_raw = trainFileReader()
	X = preprocessing.scale(X_raw.astype(float))
	y = targetToVector(y_raw)

	# Cross valitation
	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2, random_state=0)

	# Neural Network initialization
	NN = NeuralNetwork(DIMESION_OF_INPUT,28*10,10,activation='tanh', output_act = 'softmax')
	NN.fit(X_train,y_train, X_test,y_test, epochs = 10, learning_rate = .001, learning_rate_decay = .0001, verbose = 1)

	# NN predictions

	
	return 0

if __name__ == '__main__':
	main()

