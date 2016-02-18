import scipy.io
import pandas as pd
import numpy as np

mat = scipy.io.loadmat('dataLU.mat')

for k,v in mat.iteritems():
    print(k)

print(mat['dataLU'][0].shape)
print(mat['dataLU'][0][0][1][0])

#np.savetxt("dataLU.csv",mat['dataLU'],fmt="%s",delimiter=",")


#mat = {k:v for k, v in mat.items() if k[0] != '_'}

l = []

for i in range(0,31):
    l.append((i,pd.Series(mat['dataLU'][0][0][0][i])))

l.append((31,pd.Series(mat['dataLU'][0][0][1][0])))

data = pd.DataFrame({a[0]: a[1] for a in l})

data.to_csv("dataLU.csv")
