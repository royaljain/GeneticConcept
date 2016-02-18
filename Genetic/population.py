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

from random import choice as choose, sample
from random import random
import numpy as np
from sklearn.naive_bayes import GaussianNB
import Genetic.variables as v
from Genetic.individual import Individual

def dummy():
	pass

def genPop(N):

	answer = set()


	while len(answer) < N:

		#indiv = Individual([])
		#indiv.append()
		#indiv.append(0)
		answer.add(v.genCharsChrom(0))

	return list(answer)
