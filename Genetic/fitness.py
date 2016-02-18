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


def dummy():
	pass

def scoreBest(pop,SCORES):

	fittest = max(pop, key=SCORES.__getitem__)
	fittest = fittest, SCORES[fittest]

	return fittest[0].chromosomes[0].score(v.fitnessX,v.fitnessY)




def score(p, scorefuncs, scorefuncparams, SCORES):

	if p not in SCORES:
		SCORES[p] = scoreAccuracy(p)

	return SCORES[p]


def scoreAccuracy(p):

	clf = p.chromosomes[0]
	#print(type(clf))
	sc  = clf.score(v.fitnessX,v.fitnessY)
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