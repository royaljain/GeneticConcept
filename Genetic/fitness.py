'''
Copyright 2012 Ashwin Panchapakesan

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

from itertools import izip
from Genetic.individual import Individual #@UnusedImport # import only for contract checking
import variables as v
import numpy
from numpy import random 
from sklearn.metrics import f1_score,accuracy_score


def dummy():
	pass


def scoreBest2(pop,SCORES):

	cond  = v.start
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
			



	fittest = max(pop, key=SCORES.__getitem__)
	fittest = fittest, SCORES[fittest]

	#print(fittest[0].chromosomes[0].coef_)
	#print(fittest[0].chromosomes[0].intercept_)

	return fittest[0].chromosomes[0].score(mat[:,0:3],mat[:,3])




def scoreBest1(pop,SCORES):


	cond  = v.start
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
	
	'''		

	sorted(pop,key = scoreAccuracy)


	X = mat[:,0:3]
	Y = mat[:,3]

	fit1 = pop[0]
	fit2 = pop[1]
	fit3 = pop[2]
	fit4 = pop[3]
	fit5 = pop[4]

	out1 = fit1.chromosomes[0].predict(X)
	out2 = fit2.chromosomes[0].predict(X)
	out3 = fit3.chromosomes[0].predict(X)
	out4 = fit4.chromosomes[0].predict(X)
	out5 = fit5.chromosomes[0].predict(X)

	out = out1 + out2 + out3 + out4 + out5  

	for i in range(0,len(out)):
		if out[i] > 0:
			out[i] = 1
		else:
			out[i] = -1

	return accuracy_score(Y,out)

	'''

	fittest = max(pop, key=SCORES.__getitem__)
	fittest = fittest, SCORES[fittest]

	#print(fittest[0].chromosomes[0].coef_)
	#print(fittest[0].chromosomes[0].intercept_)


	#return f1_score(mat[:,3],fittest[0].chromosomes[0].predict(mat[0:2]))
	return fittest[0].chromosomes[0].score(mat[:,0:3],mat[:,3])
	

def scoreBestE(pop,SCORES):

	sorted(pop,key = scoreAccuracy)

	fit1 = pop[0]
	fit2 = pop[1]
	fit3 = pop[2]
	fit4 = pop[3]
	fit5 = pop[4]

	out1 = fit1.chromosomes[0].predict(v.fitnessX)
	out2 = fit2.chromosomes[0].predict(v.fitnessX)
	out3 = fit3.chromosomes[0].predict(v.fitnessX)
	out4 = fit4.chromosomes[0].predict(v.fitnessX)
	out5 = fit5.chromosomes[0].predict(v.fitnessX)

	out = out1 + out2 + out3 + out4 + out5  

	for i in range(0,len(out)):
		if out[i] > 0:
			out[i] = 1
		else:
			out[i] = -1

	return accuracy_score(v.fitnessY,out)
	#return f1_score(v.fitnessY,fittest[0].chromosomes[0].predict(v.fitnessX))


def scoreBest(pop,SCORES):

	fittest = max(pop, key=SCORES.__getitem__)
	fittest = fittest, SCORES[fittest]

	return fittest[0].chromosomes[0].score(v.fitnessX,v.fitnessY)
	#return f1_score(v.fitnessY,fittest[0].chromosomes[0].predict(v.fitnessX))


def score(p, scorefuncs, scorefuncparams, SCORES):

	if p not in SCORES:
		SCORES[p] = scoreAccuracy(p)

	return SCORES[p]


def scoreAccuracy(p):

	clf = p.chromosomes[0]
	#print(type(clf))
	sc  = clf.score(v.fitnessX,v.fitnessY)
	#sc = f1_score(v.fitnessY,clf.predict(v.fitnessX))
	return sc


def scoreOnes(p):
	"""
		pre:
			isinstance(p, list)
			forall(p, lambda e: isinstance(e, str))
			forall(p, lambda e: len(e)==1)
			forall(p, lambda e: e in "01")
			
		post[p]:
			p == __old__.p
			isinstance(__return__, int)
			__return__ >= 0
	"""
	return p.count('1')

def scoreTSP(tour, DIST, testmode):
	"""
		pre:
			isinstance(tour, list)
			isinstance(DIST, dict)
			forall(tour, lambda e: isinstance(e, int))
			forall(DIST, lambda k: isinstance(k, int))
			forall(DIST, lambda k: isinstance(DIST[k], dict))
			forall(DIST, lambda k: forall(DIST[k], lambda e: isinstance(e, int)))
			forall(DIST, lambda k: forall(DIST[k], lambda e: isinstance(DIST[k][e], float)))
		
		post:
			isinstance(__return__, float)
		post[tour, DIST]:
			__old__.tour == tour
			__old__.DIST == DIST
			
	"""
	answer = 0
	numcities = len(tour)
	for i,source in enumerate(tour):
		if testmode:
			assert answer <= 0
		dest = tour[(i+1)%numcities]
		answer -= DIST[source][dest]
	return answer


def evolution(p):

	for ind in p:
		clf = ind.chromosomes[0]

		clf = clf.partial_fit(v.fitnessX,v.fitnessY)
		ind.chromosomes[0] = clf