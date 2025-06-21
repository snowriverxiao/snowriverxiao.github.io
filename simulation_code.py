import random

def newvec(n=3):
    my_list = [0] * n
    random_index = random.randint(0, n - 1)  
    my_list[random_index] = 1
    return np.array(my_list)
