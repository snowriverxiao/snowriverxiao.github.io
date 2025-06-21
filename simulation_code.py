import random
import numpy as np

def newvec(n=3):
    my_list = [0] * n
    random_index = random.randint(0, n - 1)  
    my_list[random_index] = 1
    return np.array(my_list)
    
exchange = 0
Awin = 0
Bwin = 0
n = 3
times = 100000
for s in range(times):
    vec=newvec(n)
    i=random.randint(0, n - 1)
    A=vec[i]
    B=vec[-i]
    mask = np.ones(3, dtype=bool) #
    mask[i] = False
    B = vec[mask]
    j=random.randint(0, n - 2)
    if B[j] == 0:
        exchange+=1
        Awin+=A
        Bwin+=B[n-2-j]
