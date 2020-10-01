import numpy as np
import math as m 
import cmath as cm 

solutions = []
for re in np.arange(-10,10,0.01):
    for im in np.arange(-10,10,0.01):
        z = complex(re,im)
        #print(f'Checking {z}')
        if(abs(z**2 - 2**z) <= 0.01 ):
            solutions.append(np.around(z,4))

print(solutions)