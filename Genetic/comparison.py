from random import random as rand
import logging as log
import pandas as pd
import numpy as np
import pygame as pg

from random import choice as choose, sample
from random import random
import numpy as np
from sklearn.naive_bayes import GaussianNB


def comp(diff,maxGen):

	df = pd.read_csv('Genetic/Data/simStaggerData.csv',header=False)

	dfY = df.iloc[:,3]
	dfX = df.iloc[:,0:3]

	#print(dfY)
	#print(dfX)


	X = dfX.iloc[0:diff].values
	Y = dfY.iloc[0:diff].values




	l = np.random.random_integers(0,diff-1,diff/2)


	x = X[l]
	y = Y[l]


	clf =  GaussianNB()

	clf = clf.partial_fit(x,y,[-1,1])

	start = diff
	end = start + diff


	currX = dfX.iloc[start:min(end,len(dfX))].values
	currY = dfY.iloc[start:min(end,len(dfX))].values

	i = 0 
	acc = []

	while i < maxGen and end < len(dfX):

		a = clf.score(currX,currY)
		acc.append(a)
		clf = clf.partial_fit(currX,currY)
		start += diff
		end += diff

		currX = dfX.iloc[start:min(end,len(dfX))].values
		currY = dfY.iloc[start:min(end,len(dfX))].values
		i = i+1

	return acc


