

import numpy as np

from BackPropagationNN import NeuralNetwork

from sklearn import datasets
from sklearn import preprocessing
from sklearn import cross_validation
from sklearn import metrics
import csv
from numpy.numarray.session import SAVEFILE

SIZE_OF_TRAIN = 68322
SIZE_OF_TEST = 28000
DIMESION_OF_INPUT = 28*28




def trainFileReader():
	print "reading training file.."
	with open('../input/trainEx.csv', 'r') as trainFile :
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

def testFileReader():

	print "starting test file reading.."
	
	with open('../input/test.csv', 'r') as testFile :
		testReader = csv.reader(testFile, delimiter=',', quotechar='"')
		testFile.next()
		testData = np.zeros((SIZE_OF_TEST,DIMESION_OF_INPUT),dtype=float)
		print "recognizing test data.."
		for valor in xrange(SIZE_OF_TEST):
			row = testReader.next()
			matrix = np.zeros(DIMESION_OF_INPUT)
			for i in range(28*28) :
				matrix[i] = row[i]
			testData[valor] = matrix
		
#	testData = np.genfromtxt('../input/test.csv',delimiter=',',dtype='int8',skip_header=1)
	print "recognizing test data done.."

	return testData

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
	W_raw = testFileReader()
#	print 'imagen original:'
#	print W_raw[0]
	X = preprocessing.scale(X_raw.astype(float))
	y = targetToVector(y_raw)
	W = preprocessing.scale(W_raw.astype(float))
#	print 'imagen scale'
#	print W[0]
	# Cross valitation
	#X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.02, random_state=0)
	X_train = X
	y_train = y
	X_test = W
	
	
	# Neural Network initialization
	NN = NeuralNetwork(DIMESION_OF_INPUT,280,10,activation='tanh',output_act = 'softmax')
	NN.fit(X_train,y_train, epochs = 10, learning_rate = .002, learning_rate_decay = .0002, verbose = 1)

	# NN predictions
	y_predicted = NN.predict(X_test)
	"""
	for i in xrange(len(y_test)):

		print y_test[i],y_predicted[i]
	"""

	# Metrics
	y_predicted = np.argmax(y_predicted, axis=1).astype(int)
#	print y_predicted
	# y_test = np.argmax(y_test, axis=1).astype(int)
	"""
	print("\nClassification report for classifier:\n\n%s\n"
	  % (metrics.classification_report(y_test, y_predicted)))
	print("Confusion matrix:\n\n%s" % metrics.confusion_matrix(y_test, y_predicted))
	"""
	print 'prueba ok'
	
	saveFileName = 'NNPlusRelu'
	
	predictionFile = open('../output/'+saveFileName+'.csv','w')

	print "File "+saveFileName+" at ../output/"

	for i in xrange(SIZE_OF_TEST) :
		predictionFile.write(str(int(y_predicted[i])) + '\n')


	print "DataDigitRecognizing save at ",'../output/'+saveFileName+'.csv'

	print "DigitRecognizing done.."
	predictionFile.close()

	print "Initializing CSV Converting.."
	fileDigitRecognizeConvertToCVS(saveFileName)
	print "CSV Converting done.."

def fileDigitRecognizeConvertToCVS(saveFileName):
	predictionFile = open('../output/'+saveFileName+'.csv','r')

	predictionFileCVS = open('../output/'+saveFileName+'Kg.csv','w')

	predictionFileCVS.write('"ImageId","Label"\n')

	i = 1
	for label in predictionFile:
		predictionFileCVS.write(str(i)+','+'"'+ str(int(label)) +'"\n')
		i+=1

	predictionFileCVS.close()
	predictionFile.close()
	return 0

if __name__ == '__main__':
	main()

