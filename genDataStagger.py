import numpy as numpy
from numpy import random 


examples = 120

features = 3


mat = numpy.zeros((examples,features+1))

for i in range(0,examples):

	x1 = random.randint(0,3)
	x2 = random.randint(0,3)
	x3 = random.randint(0,3)

	mat[i][0] = x1
	mat[i][1] = x2
	mat[i][2] = x3

	if i < 40:
		if x1 == 2 and x3 == 0:
			mat[i][3] = 1
		else:
			mat[i][3] = -1

	elif i < 80:
		if x1 == 0 or x2 == 1:
			mat[i][3] = 1
		else:
			mat[i][3] = -1

	elif i < 37500:
		if x3 == 1 and x3 == 2:
			mat[i][3] = 1
		else:
			mat[i][3] = -1
		


numpy.savetxt("Genetic/Data/simStaggerData.csv",mat,fmt="%d",delimiter=",")