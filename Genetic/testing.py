import numpy as np
import math

def cross4(u,w,c1,c2):


	modu = np.linalg.norm(u)
	modw = np.linalg.norm(w)
	
	u = u/modu
	w = w/modw

	a = np.dot(u,w)

	if a >= 1 or a <= -1:
		
		print(u)

	else:	
		
		degree = math.acos(a)

		tot = c1+c2

		ang = c1*degree/(c1+c2)

		print(ang)

		w_ = w - (u*(np.dot(u,w)))

		print(w_)

		w_ = w_/(np.linalg.norm(w_))



		result = math.cos(ang) * u + math.sin(ang) * w_

		result = result/np.linalg.norm(result)

		print(result)


a = np.array([2,0])
b = np.array([0,3])

cross4(a,b,2,1)
