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
import random
import math
import numpy as np
from random import randint, choice as choose, sample, shuffle
from Genetic.individual import Individual

def mutate1(p,s,Y):

	clf = p.chromosomes[0]

	mat = clf.theta_


	for i in range(0,len(mat)):
		for j  in range(0,len(mat[0])):
			if random.random() < 0.5:
				mat[i][j] = 0.5* mat[i][j]
			else:
				mat[i][j] = 2* mat[i][j]

	clf.theta_ = mat

	p.chromosomes[0] = clf

	answer = Individual(p.chromosomes[:])

	return answer


def mutate2(p,s,Y):

	clf = p.chromosomes[0]

	pri1 = clf.class_prior_

	
	pri2 = [ sum(Y==1),sum(Y==-1) ]

	su = sum(pri2)

	pri2 = np.array(pri2)

	pri2 = pri2/(1.0*su)

	pr = s*pri1 + (1-s)*pri2

	clf.class_prior_ = pr

	p.chromosomes[0] = clf

	answer = Individual(p.chromosomes[:])
	
	return answer

def mutate3(p,s,Y):

	
	if random.random() < 0.5:
		p.chromosomes[0].coef_ = s* p.chromosomes[0].coef_
		p.chromosomes[0].intercept_ = s* p.chromosomes[0].intercept_
	
	else:
		p.chromosomes[0].coef_ = (2-s)* p.chromosomes[0].coef_
		p.chromosomes[0].intercept_ = (2-s)* p.chromosomes[0].intercept_

	answer = Individual(p.chromosomes[:])
	
	return answer


def mutate4(p,s,Y):

		
	if random.random() < 0.5:
		p.chromosomes[0].coef_ = s* p.chromosomes[0].coef_
	
	else:
		p.chromosomes[0].coef_ = (2-s)* p.chromosomes[0].coef_

	answer = Individual(p.chromosomes[:])
	
	return answer

def mutate5(p,s,Y):


	ang = 1.57*(1-s)
	
	u  = p.chromosomes[0].coef_ = s* p.chromosomes[0].coef_[0]


	n = len(u)

	d =  random.random()

	for i in range(0,n):
		if d < i/(1.0/n):

			k = np.zeros((n,0))
			k[i] = 1

			result =  u*math.cos(ang) + np.cross(k,u)*math.sin(ang) + k*(np.dot(k,u))(1-math.cos(ang))	
			p_new1.chromosomes[0].coef_ = np.array([result])
			break
	

	answer = Individual(p.chromosomes[:])
	
	return answer
