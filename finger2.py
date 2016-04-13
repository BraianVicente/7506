#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  finger2.py
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

from sklearn import neighbors
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

def trainFileReader():
	print "reading training file.."
	with open('Documentos/Finger1/input/trainPlus.csv', 'r') as trainFile :
		trainReader = csv.reader(trainFile, delimiter=',', quotechar='"')
		trainFile.next()

		trainData = []
		trainTarget = np.zeros(68870)
		j = 0
		print "recognize file data.."

		for row in trainReader :
			matrix = np.zeros(28*28)
			trainTarget[j] = row[0]
			for i in range(28*28) :
				matrix[i] = row[i+1]

			trainData.append(matrix)
			j+=1
		print "recognize file data done.."
		return [trainData,trainTarget]

def testFileReader():

	print "starting test file reading.."
	with open('Documentos/Finger1/input/test.csv', 'r') as testFile :
		testReader = csv.reader(testFile, delimiter=',', quotechar='"')
		testFile.next()
		testData = []
		print "recognizing test data.."
		for row in testReader :
			matrix = np.zeros(28*28)
			for i in range(28*28) :
				matrix[i] = row[i]

			testData.append(matrix)
	print "recognizing test data done.."

	return testData

def digitRecognizeKaggleWhitKNeigbours(kNeigbours,saveFileName):
	digitRecognizeKaggle(saveFileName,neighbors.KNeighborsClassifier(n_neighbors=kNeigbours))

def digitRecognizeKaggle(saveFileName='trainPlusDefault',kNeigboursClassifier=neighbors.KNeighborsClassifier()):
	trainFileData = trainFileReader()
	trainData = trainFileData[0]
	trainTarget = trainFileData[1]

#~ Aqui se entrena el set de datos.
	print "starting knn DigitRecorgnize train.."
	knnDigitRecorgnize = kNeigboursClassifier
	print "training knnDigitRecorgnize.."
	knnDigitRecorgnize.fit(trainData,trainTarget)
	print "training knnDigitRecorgnize done.."

	testData = testFileReader()

	print "starting DigitRecognizing.."
	predictionFile = open('Documentos/Finger1/input/'+saveFileName+'.csv','w')
	#~ print knnDigitRecorgnize.predict([testData[0]])
	#~ print str(knnDigitRecorgnize.predict([testData[0]])[0])
	#~ print int(knnDigitRecorgnize.predict([testData[0]])[0])
	print "File "+saveFileName+"at Documentos/Finger1/input/"
	i = 0
	j = 2800
	for row in testData :
		predictionFile.write(str(int(knnDigitRecorgnize.predict([row])[0])) + '\n')
		if (i%j == 0) :
			print "DigitRecognize: %",float(i/280)
		i+=1

	print "DataDigitRecognizing save at ",'Documentos/Finger1/input/'+saveFileName+'.csv'

	print "DigitRecognizing done.."
	predictionFile.close()

	print "Initializing CSV Converting.."
	fileDigitRecognizeConvertToCVS(saveFileName)
	print "CSV Converting done.."

def fileDigitRecognizeConvertToCVS(saveFileName):
	predictionFile = open('Documentos/Finger1/input/'+saveFileName+'.csv','r')

	predictionFileCVS = open('Documentos/Finger1/input/'+saveFileName+'knn.csv','w')

	predictionFileCVS.write('"ImageId","Label"\n')

	i = 1
	for label in predictionFile:
		predictionFileCVS.write(str(i)+','+'"'+ str(int(label)) +'"\n')
		i+=1

	predictionFileCVS.close()
	predictionFile.close()

def main():

	if len(sys.argv) > 1 :
		kdistance = int(sys.argv[1])
		filename = sys.argv[2]
		digitRecognizeKaggleWhitKNeigbours(kdistance,filename)
	else :
		digitRecognizeKaggle()
	return 0

if __name__ == '__main__':
	main()

