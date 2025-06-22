import random
import numpy as np

def newvec(n=3):
    my_list = [0] * n
    random_index = random.randint(0, n - 1)  
    my_list[random_index] = 1
    return np.array(my_list)
    
switching = 0
Awin = 0
Bwin = 0
n = 3
times = 100000

for s in range(times):
    vec = newvec(n)
    i = random.randint(0, n - 1)
    A = vec[i]
    B = vec[-i]
    mask = np.ones(n, dtype=bool) 
    mask[i] = False
    B = vec[mask]
    shuffled_indices = np.random.permutation(n-1)
    random_indices = shuffled_indices[:n-2]
    if np.sum(B[random_indices]) == 0:
        switching += 1
        Awin += A
        Bwin += B[shuffled_indices[n-2]]
        
print(f"The probability of winning with the initial choice {Awin/switching}")
print(f"The probability of winning with the switching {Bwin/switching}")
