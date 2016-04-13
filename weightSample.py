from sklearn import neighbors
import matplotlib.pyplot as plt
import numpy as np
from finger2 import trainFileReader

def weighOfImage(row):
	summarize = 0
	i,j = 0,0
	for value in row :
		if value != 0 :
			j+=1
		i+=1
	return float(j)/float(i)

array = trainFileReader()
dataArray = array[0]
targetArray = array[1]
listOfWeights = [weighOfImage(row) for row in dataArray]
listOfWeights.sort(reverse=True)
summarizeOfWeights=0
for i in xrange(len(listOfWeights)):
	summarizeOfWeights+=listOfWeights[i]
	j = i+1
print summarizeOfWeights/j,summarizeOfWeights,j



def classesTotal(dataArray,targetArray) :
	classesTotal =  [0,0,0,0,0,0,0,0,0,0]
	for element in targetArray :
		classesTotal[int(element)]+=1
		row = dataArray[i]
		i+=1
		for value in row:
			dataContainer[int(element)]+=value

def calcularPromedioClases():

	dataContainer = [0,0,0,0,0,0,0,0,0,0]
	i = 0



	for i in xrange(0,9):
		print int(dataContainer[i]/dataSumarizer[i])

