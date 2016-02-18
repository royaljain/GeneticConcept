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

from Genetic.individual import Individual
from random import randint, sample
import numpy as np
import Genetic.variables as v
import math

def dummy():
	pass

def cross_old(p1,p2,i):

	p_new1 = v.genCharsChrom(i)
	p_new2 = v.genCharsChrom(i)
	p_new3 = v.genCharsChrom(i)
	p_new4 = v.genCharsChrom(i)

	p_new1.chromosomes[0].class_prior_ = p1.chromosomes[0].class_prior_
	p_new1.chromosomes[0].class_count_ = p1.chromosomes[0].class_count_
	p_new1.chromosomes[0].theta_ = p1.chromosomes[0].theta_
	p_new1.chromosomes[0].sigma_ = p1.chromosomes[0].sigma_



	p_new2.chromosomes[0].class_prior_ = p2.chromosomes[0].class_prior_
	p_new2.chromosomes[0].class_count_ = p2.chromosomes[0].class_count_
	p_new2.chromosomes[0].theta_ = p2.chromosomes[0].theta_
	p_new2.chromosomes[0].sigma_ = p2.chromosomes[0].sigma_


	return p_new1,p_new2,p_new3,p_new4


def cross1(p1,p2,i,c1,c2):

	p_new1 = v.genCharsChrom(i)
	p_new2 = v.genCharsChrom(i)

	tot = c1+c2

	c1 = c1/(1.0*tot)
	c2 = c2/(1.0*tot)


	p_new1.chromosomes[0].class_prior_ = c1*p1.chromosomes[0].class_prior_ + c2*p2.chromosomes[0].class_prior_
	p_new1.chromosomes[0].class_count_ = c1*p1.chromosomes[0].class_count_ + c2*p2.chromosomes[0].class_count_
	p_new1.chromosomes[0].theta_ = c1*p1.chromosomes[0].theta_ + c2*p2.chromosomes[0].theta_
	p_new1.chromosomes[0].sigma_ = c1*c1*p1.chromosomes[0].sigma_ + c2*c2*p2.chromosomes[0].sigma_


	return [p_new1,p_new2]


def cross2(p1,p2,i,c1,c2):

	p_new1 = v.genCharsChrom(i)
	p_new2 = v.genCharsChrom(i)


	return [p_new1,p_new2]




def cross3(p1,p2,i,c1,c2):

	p_new1 = v.genCharsChrom(i)
	p_new2 = v.genCharsChrom(i)

	tot = c1+c2

	c1 = c1/(1.0*tot)
	c2 = c2/(1.0*tot)


	p_new1.chromosomes[0].coef_ = c1*p1.chromosomes[0].coef_ + c2*p2.chromosomes[0].coef_
	p_new1.chromosomes[0].intercept_ = c1*p1.chromosomes[0].intercept_ + c2*p2.chromosomes[0].intercept_

	return [p_new1,p_new2]



def cross4(p1,p2,i,c1,c2):


	p_new1 = v.genCharsChrom(i)
	p_new2 = v.genCharsChrom(i)

	u = p1.chromosomes[0].coef_[0]
	w = p2.chromosomes[0].coef_[0]


	modu = np.linalg.norm(u)
	modw = np.linalg.norm(w)
	
	u = u/modu
	w = w/modw

	#print(u)
	#print(w)


	a = np.dot(u,w)

	if a >= 1 or a <= -1:

		return [p_new1,p_new2]

	else:	

		#print(a)
		degree = math.acos(a)

		tot = c1+c2

		ang = c1*degree/(c1+c2)


		

		w_ = w - (u*(np.dot(u,w)))

		w_ = w_/(np.linalg.norm(w_))


		#print(ang)

		result = math.cos(ang) * u + math.sin(ang) * w_

		p_new1.chromosomes[0].coef_ = np.array([result])

		#print(p_new1.chromosomes[0].coef_)
		#print(p_new2.chromosomes[0].coef_)
		
		return [p_new1,p_new2]


