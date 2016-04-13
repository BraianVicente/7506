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
