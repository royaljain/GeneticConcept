from random import choice as choose, sample
from random import random
import numpy as np
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import matplotlib.pyplot as plt
import Genetic.comparison as comparison
from Genetic.individual import Individual


PopGenX,PopGenY,fitnessX,fitnessY,start,end ,df,dfX, dfY, delta , lis,nam,maxGens,f,readfile,writefile = [0]*16

def init(diff,m):

	global PopGenX,PopGenY,fitnessX,fitnessY,start,end ,df,dfX, dfY, delta , lis,nam,maxGens,f,readfile,writefile

	readfile = 'Genetic/Data/dataLU.csv'
	writefile = "Genetic/Results/LUDataresults.txt"


	df = pd.read_csv(readfile,header=True)
	f = open(writefile,"w")

	nam = []
	lis = []

	dfY = df.iloc[:,32]
	dfX = df.iloc[:,1:32]

	print(dfY)
	print(dfX)

	delta = diff
	maxGens = m
	start = delta
	end = start + delta 


	PopGenX = dfX.iloc[0:start].values
	PopGenY = dfY.iloc[0:start].values

	fitnessX = dfX.iloc[0:start].values
	fitnessY = dfY.iloc[0:start].values

def genCharsChrom(genNum):
	
	global PopGenX,PopGenY,fitnessX,fitnessY,start,end ,df,dfX, dfY, delta , lis,nam,maxGens,f
	
	size = len(PopGenX)

	#print(size)

	l = np.random.random_integers(0,size-1,size/2)

	x = PopGenX[l]
	y = PopGenY[l]


	clf =  GaussianNB()

	clf = clf.partial_fit(x,y,[1,-1])

	return Individual([clf,genNum])


def forward():


	global PopGenX,PopGenY,fitnessX,fitnessY,start,end ,df,dfX, dfY, delta , lis,nam,maxGens,f
	PopGenX = fitnessX 
	PopGenY = fitnessY

	start += delta
	end += delta

	fitnessX = dfX.iloc[start:min(end,len(dfX))].values
	fitnessY = dfY.iloc[start:min(end,len(dfX))].values


	if end < len(dfX):
		return True
	else:
		return False



def writeToFile(na,an):

	global PopGenX,PopGenY,fitnessX,fitnessY,start,end ,df,dfX, dfY, delta , lis,nam,maxGens,f
	

	z  = zip(na,an)

	for name,answer in z:

		f.write(name + "," + str(sum(answer)/len(answer)) + "\n")
		f.write(str(answer) + "\n")
		#f.flush()
		l = range(1,len(answer)+1)	
		plo, = plt.plot(l,answer,label=name)

		nam.append(name)
		lis.append(plo)


	f.flush()


def runComp(diffv):

	global PopGenX,PopGenY,fitnessX,fitnessY,start,end ,df,dfX, dfY, delta , lis,nam,maxGens,f

	for values in diffv:

		answer = comparison.comp(values,maxGens)
		name = "Comparison" + str(values)

		l = range(1,len(answer)+1)	
		plo, = plt.plot(l,answer,label=name)

		nam.append(name)
		lis.append(plo)

		f.write(name + ":" + str(sum(answer)/len(answer)) + "\n")
		f.write(str(answer) + "\n")
		f.flush()
		print(name + "," + str(sum(answer)/len(answer)) + "\n")

	f.close()

	#plotGraphs()


def plotGraphs():

	global PopGenX,PopGenY,fitnessX,fitnessY,start,end ,df,dfX, dfY, delta , lis,nam,maxGens,f
	plt.legend(lis,nam)
	plt.show()