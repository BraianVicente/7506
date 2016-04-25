#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  kaggleSet.py
#
#  Copyright 2016 Braian Hernán Vicente <brahvic@Lenovo-G580>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import numpy as np

from BackPropagationNN import NeuralNetwork

from sklearn import datasets
from sklearn import preprocessing
from sklearn import cross_validation
from sklearn import metrics
import csv

SIZE_OF_TRAIN = 1200
DIMESION_OF_INPUT = 28*28


def trainFileReader():
	print "reading training file.."
	with open('../input/train.csv', 'r') as trainFile :
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
		a[i,x[i]] = 1
	return a

def main():

	# Digits dataset loading
	# digits = datasets.load_digits()
	X_raw, y_raw = trainFileReader()
	X = preprocessing.scale(X_raw.astype(float))
	y = targetToVector(y_raw)

	# Cross valitation
	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.02, random_state=0)

	# Neural Network initialization
	NN = NeuralNetwork(DIMESION_OF_INPUT,28*10,10, output_act = 'softmax')
	NN.fit(X_train,y_train, epochs = 10, learning_rate = .001, learning_rate_decay = .0001, verbose = 1)

	# NN predictions
	y_predicted = NN.predict(X_test)
	for i in xrange(len(y_test)):

		print y_test[i],y_predicted[i]

	# Metrics
	y_predicted = np.argmax(y_predicted, axis=1).astype(int)
	y_test = np.argmax(y_test, axis=1).astype(int)

	print("\nClassification report for classifier:\n\n%s\n"
	  % (metrics.classification_report(y_test, y_predicted)))
	print("Confusion matrix:\n\n%s" % metrics.confusion_matrix(y_test, y_predicted))

	return 0

if __name__ == '__main__':
	main()

