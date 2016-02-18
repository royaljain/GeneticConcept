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

from Genetic import fitness, selection, mutation, crossover, population

from collections import defaultdict
from math import sqrt
from itertools import count

import pygame as pg #@UnresolvedImport

def listOfSettings():

	cross  = [(crossover.cross3,"CROSS3"),(crossover.cross4,"CROSS4")]
	mut  = [(mutation.mutate4,"MUT4"),(mutation.mutate3,"MUT3")]
	diff = [50,100,200]
	
	#cross  = [(crossover.cross1,"CROSS1")]
	#mut  = [(mutation.mutate2,"MUT2")]
	#diff = [50]


	l = []

	for c in cross:
		for m in mut:
			for d in diff:
				l.append((getOneMaxSettings(c[0],m[0],d),c[1]+m[1]+str(d)))

	return l
				




def getOneMaxSettings(c,m,d):
	
	maxGens = 1001
	targetscore = 30
	popsize = 100
	alleles0 = '01'
	chromlen0 = 30
	numCrossovers = popsize
	SCORES = {}
	diff = d
	genfunc = population.genPop
	genparams = (popsize)
	
	scorefunc = fitness.score
	scoreparams = ([fitness.scoreOnes], [()], SCORES)
	
#	selectfunc = selection.tournamentSelect
#	tournsize = 10
#	numwinners = 1
#	numselect = 2
#	selectparams = (tournsize, numwinners, numselect, scorefunc, scoreparams)
	
	selectfunc = selection.rouletteWheelSelect
	selectparams = ()
	
	crossprob = 0.9
	mutprob = 0.05
	
	crossfunc = c
	crossparams = (0,)
	
	mutfunc = m
	mutparams = (0, alleles0)
	
	rouletteWheelRequireres = {selection.rouletteWheelSelect}
	getWheel = selectfunc in rouletteWheelRequireres
	
	sanity = """maxGens targetscore SCORES diff
				genfunc genparams
				scorefunc scoreparams 
				selectfunc selectparams 
				crossfunc crossparams crossprob numcross
				mutfunc mutparams mutprob 
				getWheel""".split()
	answer = {
			'maxGens' : maxGens,
			'targetscore' : targetscore,
			'SCORES' : SCORES,
			'diff' : diff,
			'genfunc' : genfunc,
			'genparams' : genparams,
			'inputs' : genparams,
			'scorefunc' : scorefunc,
			'scoreparams' : scoreparams,
			'selectfunc' : selectfunc,
			'selectparams' : selectparams,
			'crossfunc' : crossfunc,
			'crossprob' : crossprob,
			'numcross' : numCrossovers,
			'crossparams' : crossparams,
			'mutfunc' : mutfunc,
			'mutparams' : mutparams,
			'mutprob' : mutprob,
			'getWheel' : getWheel,
			'sanity' : sanity
			}
	return answer
