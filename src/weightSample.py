#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  weightSample.py
#  
#  Copyright 2016 champaine <champaine@Champaine-Desktop>
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

