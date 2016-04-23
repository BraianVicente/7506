#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  datamerge.py
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

import sys
import fileconvert
import finger2

def simillitudeBetthenFiles(file_1,file_2):
	file_1 = open('Documentos/Finger1/input/'+file_1+'.csv','r')

	file_2 = open('Documentos/Finger1/input/'+file_2+'.csv','r')

	i = 1
	j = float(0)
	for row_1 in file_1 :

		row_2 = file_2.readline()
		if (int(row_1)==int(row_2)) : j+=1
		i+=1
	i-=1
	print j/i
	file_1.close()
	file_2.close()

def equalsValues():
	nameList = ['prediction','kDistance2','kDistance3','kDistance4','kDistance6','kDistance8','kDistance12']
	file_1 = open('Documentos/Finger1/input/'+nameList[0]+'.csv','r')
	file_2 = open('Documentos/Finger1/input/'+nameList[1]+'.csv','r')
	file_3 = open('Documentos/Finger1/input/'+nameList[2]+'.csv','r')
	file_4 = open('Documentos/Finger1/input/'+nameList[3]+'.csv','r')
	file_5 = open('Documentos/Finger1/input/'+nameList[4]+'.csv','r')
	file_6 = open('Documentos/Finger1/input/'+nameList[5]+'.csv','r')
	file_7 = open('Documentos/Finger1/input/'+nameList[6]+'.csv','r')

	l1 = file_1.readlines()
	l2 = file_2.readlines()
	l3 = file_3.readlines()
	l4 = file_4.readlines()
	l5 = file_5.readlines()
	l6 = file_6.readlines()
	l7 = file_7.readlines()

	file_1.close()
	file_2.close()
	file_3.close()
	file_4.close()
	file_5.close()
	file_6.close()
	file_7.close()
	j = 0
	trainPlus=[]
	for i in xrange(28000):
		if int(l1[i])==int(l2[i])==int(l3[i])==int(l4[i])==int(l5[i])==int(l6[i])==int(l7[i]) :
			trainPlus.append((i+1,int(l1[i])))



	trainFile = open('Documentos/Finger1/input/train.csv','r')
	fileTest =  open('Documentos/Finger1/input/test.csv','r')
	archTrainPlus = open('Documentos/Finger1/input/trainPlus.csv','w')


	for line in trainFile :
		archTrainPlus.write(line)

	listTestFile = fileTest.readlines()
	#~ listComplet = []

	for i in xrange(len(trainPlus)):

		j = int(trainPlus[i][0])
		string = str(int(trainPlus[i][1]))+','+listTestFile[j]
		archTrainPlus.write(string)
		#~ listComplet.append((int(trainPlus[i][1]),listTestFile[j-1]))
	#~ print fileTest[0]
	print string
	#~ i = 1
	#~ for value_data in trainPlus:
		#~ archTrainPlus.write(str(value_data[0])+','+ str(value_data[1]) +'"\n')
		#~ i+=1

	trainFile.close()
	archTrainPlus.close()
	fileTest.close()
def mayorProbabilidad(lista):
	listaConTotales = [0,0,0,0,0,0,0,0,0,0]
	for i in lista:
		listaConTotales[i]+=1
	mayorProba = listaConTotales[0]
	mayorIndex = 0
	while i < 10:
		if (mayorProba < listaConTotales[i]):
			mayorProba = listaConTotales[i]
			mayorIndex = i
		i+=1

	print mayorIndex,listaConTotales
	return mayorIndex


def main():
	#~ list_1 = ['prediction','kDistance2','kDistance3','kDistance4','kDistance6','kDistance8','kDistance12']
	#~ list_2 = ['prediction','kDistance2','kDistance3','kDistance4','kDistance6','kDistance8','kDistance12']
	#~ for name_1 in list_1 :
		#~ for name_2 in list_2:
			#~ simillitudeBetthenFiles(name_1,name_2)
	equalsValues()
	return 0

if __name__ == '__main__':
	main()

