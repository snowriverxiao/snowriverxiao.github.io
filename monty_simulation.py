import random
import numpy as np
import argparse

def newvec(n=3):
    my_list = [0] * n
    random_index = random.randint(0, n - 1)  
    my_list[random_index] = 1
    return np.array(my_list)
    

def main(n, times,randomHost): ## times is the simulation times, n is the number of doors
    switching = 0
    Awin = 0
    Bwin = 0

    if randomHost == 1:
        for _ in range(times):
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
    else:
        for _ in range(times):
            vec = newvec(n)
            i = random.randint(0, n - 1)
            A = vec[i]
            B = vec[-i]
            mask = np.ones(n, dtype=bool) 
            mask[i] = False
            B = vec[mask]
            switching += 1
            Awin += A
            Bwin += np.sum(B)
        
    print(f"The probability of winning with the initial choice {Awin/switching}")
    print(f"The probability of winning with the switching {Bwin/switching}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monty Hall Simulation")
    parser.add_argument('--n', type=int, default=3, help="Number of doors")
    parser.add_argument('--times', type=int, default=100000, help="Number of simulations")
    parser.add_argument('--randomHost', type=int, default=1,  help="Host randomly open door")

    args = parser.parse_args()
    
    main(args.n, args.times,args.randomHost)

