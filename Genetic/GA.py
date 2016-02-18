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

from Genetic import settings, selection, visualization as vis
from Genetic import mutation, crossover, fitness, individual, population #@UnusedImport # for contract checking only
from Genetic.individual import Individual #@UnusedImport # for contract checking only
from random import random as rand
import logging as log
import pandas as pd
from sets import Set
import numpy as np
import pygame as pg #@UnresolvedImport
import Genetic.variables as v
import matplotlib.pyplot as plt


log.basicConfig(format='%(levelname)s|%(message)s', level=log.DEBUG)


def runGA(kwargs, testmode=False):
	"""
		pre:
			isinstance(kwargs, dict)
			'maxGens' in kwargs
			kwargs['maxGens'] > 0
		
		post[kwargs]:
			__old__.kwargs == kwargs
			__return__[0][1] >= kwargs['targetscore'] or __return__[1] == kwargs['maxGens']
			isinstance(__return__[0][0], Individual)
	"""
	
	if 'sanity' not in kwargs:
		raise TypeError("Expected argument 'sanity' not found")
	arguments = kwargs['sanity']
	
	if len(kwargs) < len(arguments):
		raise TypeError("Missing Arguements: %s" %' '.join([a for a in arguments if a not in kwargs]))
	
	# # # # # # PARAMETERS # # # # # #
	
	maxGens = kwargs['maxGens']
	targetscore = kwargs['targetscore']
	genfunc = kwargs['genfunc']
	genparams = kwargs['genparams']

	scorefunc = kwargs['scorefunc']
	scoreparams = kwargs['scoreparams']

	selectfunc = kwargs['selectfunc']
	selectparams = kwargs['selectparams']
	
	numcross = kwargs['numcross']
	crossfunc = kwargs['crossfunc']
	crossprob = kwargs['crossprob']
	crossparams = kwargs['crossparams']

	mutfunc = kwargs['mutfunc']
	mutprob = kwargs['mutprob']
	mutparams = kwargs['mutparams']
	
	SCORES = kwargs['SCORES']
	diff = kwargs['diff']
	getWheel = kwargs['getWheel']

	crossover.dummy()
	fitness.dummy()
	population.dummy()

	v.init(diff,maxGens)

	#print(len(v.PopGenX))

	# # # # # # /PARAMETERS # # # # # #
	


	


	pop = genfunc(genparams)

	N = len(pop)

	for p in pop:
		if p not in SCORES:
			SCORES[p] = scorefunc(p, *scoreparams)


	
	best = max(SCORES, key=SCORES.__getitem__)
	best = best, SCORES[best]	# indiv, score
	
	g = 1


	acc = []

	b = True

	while  g < maxGens and b:

		if( g % 50 == 0):
			print(str(g))


		if testmode:
			assert g < maxGens
			assert best[1] < targetscore

		if getWheel:
			wheel = selection.getRouletteWheel(pop, SCORES)
		
		newpop = []



		for _ in xrange(numcross):
			
			if getWheel:
				p1 = selectfunc(wheel, *selectparams)
				p2 = selectfunc(wheel, *selectparams)
			else:
				p1, p2 = selectfunc(pop, *selectparams)
			

			if rand() <= crossprob:
				l = crossfunc(p1,p2,g,SCORES[p1],SCORES[p2])
				
				for a in l:
					SCORES[a] = scorefunc(a, *scoreparams)	

				newpop.extend(l)			
				
			else:
				newpop.extend([p1,p2])			

		
		for i,p in enumerate(newpop):
			if rand() <= mutprob:
				newpop[i] = mutfunc(p,SCORES[p],v.PopGenY)
				p = newpop[i]
			SCORES[p] = scorefunc(p, *scoreparams)
		
		pop = newpop

		sorted(pop,key = fitness.scoreAccuracy)

		pop = pop[0:N]
		

		b = v.forward()

		a = fitness.scoreBest(pop,SCORES)		
		
		acc.append(a) 
		
		fitness.evolution(pop)
		g += 1

	
	if testmode:
		assert (g == maxGens)
	

	return acc


if __name__ == "__main__":
	print 'starting'

	
	diffv = Set()

	nam = []
	ans = []

	for setting,name in settings.listOfSettings():

		answer = runGA(setting)
		diffv.add(setting['diff'])

		print(name + "," + str(sum(answer)/len(answer)) + "\n")
		
		nam.append(name)
		ans.append(answer)


	v.writeToFile(nam,ans)
	v.runComp(diffv)

	print 'done'
