import numpy as np


def NextFib(no):

    eigenvalue = np.linalg.eigvals(np.array(((1,1),(1,0))))
    Nextval = np.around(no*eigenvalue[0],0)
    PrevVal = np.around(no/eigenvalue[0],0)
    return [Nextval,PrevVal,eigenvalue]

x=75025
while(x<100000000000000000):
    le = NextFib(x)[0]
    print(x = NextFib(x))
    x = le

print(f'Golden Ratio : {NextFib(75025)[2][0]}')



