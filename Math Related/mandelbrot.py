import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image

def convergencetester(i,j,frameno):
    c = complex(i, j) 
    z = complex(0,0)
    for i in range(1, 50): 
        if abs(z) > 2: 
            return True
        z = pow(z,frameno) + c
    return False

print("[#", end ="") 
for fram in range(30,600):
    mainmat = np.zeros((500,500))
    for x in range(0,500):
        for y in range(0,500):
            if(convergencetester(y/250 -1.5 , x/250 -1 ,fram/60)):
                mainmat[x][y] = 1
    plt.imshow(mainmat)
    imname = 'comp_'+str(fram)+'.png'
    plt.savefig(imname, bbox_inches='tight')
    if(fram%60==0):
        print("#", end ="") 

print("]", end ="") 

'''
for fram in range(0,60):
    mainmat = np.zeros((1000,1000))
    for x in range(0,1000):
        for y in range(0,1000):
            if(convergencetester(y/500 -1.5 , x/500 -1 , fram/10)):
                mainmat[x][y] = 1
    plt.imshow(mainmat)
'''