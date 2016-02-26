from random import random as rand
import logging as log
import pandas as pd
import numpy as np
import pygame as pg
from sklearn.metrics import f1_score,accuracy_score
from random import choice as choose, sample
from random import random
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.linear_model import SGDClassifier
import fitness
import numpy
from numpy import random 

def scoreBest2(clf,cond):

	examples = 100
	features = 3
	mat = numpy.zeros((examples,features+1))

	for i in range(0,examples):

		x1 = random.random()*10.0;
		x2 = random.random()*10.0;
		x3 = random.random()*10.0; 

		mat[i][0] = x1
		mat[i][1] = x2
		mat[i][2] = x3

		if cond < 12500:
			b = 8

		elif cond < 25000:
			b = 9

		elif cond < 37500:
			b = 7

		else:
			b = 9.5



		if x1 + x2 <= b: 
			mat[i][3] = 1
		else:
			mat[i][3] = -1
			

	return f1_score(mat[:,3],clf.predict(mat[:,0:3]))
	#return clf.score(mat[:,0:3],mat[:,3])


def scoreBest(clf,cond):


	examples = 100
	features = 3
	mat = numpy.zeros((examples,features+1))

	for i in range(0,examples):

		x1 = random.randint(0,3)
		x2 = random.randint(0,3)
		x3 = random.randint(0,3)

		mat[i][0] = x1
		mat[i][1] = x2
		mat[i][2] = x3

		if cond < 40:
			if x1 == 2 and x3 == 0:
				mat[i][3] = 1
			else:
				mat[i][3] = -1

		elif cond < 80:
			if x1 == 0 or x2 == 1:
				mat[i][3] = 1
			else:
				mat[i][3] = -1

		elif cond < 120:
			if x3 == 1 and x3 == 2:
				mat[i][3] = 1
			else:
				mat[i][3] = -1
			

	return clf.score(mat[:,0:3],mat[:,3])

def comp(diff,maxGen):

	df = pd.read_csv('Genetic/Data/simStaggerData.csv',header=False)

	dfY = df.iloc[:,3]
	dfX = df.iloc[:,0:3]

	dfX = (dfX - dfX.mean())

	#print(dfY)
	#print(dfX)


	X = dfX.iloc[0:diff].values
	Y = dfY.iloc[0:diff].values




	l = np.random.random_integers(0,diff-1,diff/2)


	x = X[l]
	y = Y[l]


	#clf =  PassiveAggressiveClassifier(fit_intercept = True)
	clf =  PassiveAggressiveClassifier(fit_intercept = False)
	#clf =  GaussianNB()


	clf = clf.partial_fit(x,y,[-1,1])

	start = diff
	end = start + diff


	currX = dfX.iloc[start:min(end,len(dfX))].values
	currY = dfY.iloc[start:min(end,len(dfX))].values

	i = 0 
	acc = []

	while i < maxGen and end < len(dfX):

		a = scoreBest(clf,start)
		#a = clf.score(currX,currY)
		#a = f1_score(currY,clf.predict(currX))
		acc.append(a)
		clf = clf.partial_fit(currX,currY)
		start += diff
		end += diff

		currX = dfX.iloc[start:min(end,len(dfX))].values
		currY = dfY.iloc[start:min(end,len(dfX))].values
		i = i+1

	return acc


'''
a = comp(50,4000)
b = comp(100,4000)
c = comp(200,4000)



print(sum(a)/len(a))
print(sum(b)/len(b))
print(sum(c)/len(c))
'''