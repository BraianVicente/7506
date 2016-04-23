#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fileconvert.py
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
import sys


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


import csv

def cvsToTextPlane():
	with open('Documentos/Finger1/input/knn.csv','r') as knn :
		knnReader = csv.reader(knn, delimiter=',', quotechar='"')
		knn.next()

		newFile = open('Documentos/Finger1/input/Otherknn.csv','w')

		for row in knnReader:
			newFile.write(str(int(row[1]))+'\n')

		newFile.close()

def main():

	if len(sys.argv) > 1 :
		fileDigitRecognizeConvertToCVS(sys.argv[1])
	else:cvsToTextPlane()
	return 0

if __name__ == '__main__':
	main()
