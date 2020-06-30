import random as rand
import numpy as np
import matplotlib.pyplot as plt
import timeit

def numberOneA(count):
    
    dict = set()
    result = 0
    for i in range(0, count):
        prevLen = len(dict)
        dict.add(rand.randint(0 ,5000))
        if(len(dict) == prevLen):
            break
        else:
            result = result + 1
    return result



#for number two

def numberOneB(n, m):
  
    storage = np.zeros(m)
   
    for i in range(0, m):
        storage[numberOneA(n)] +=  1

    
    data = np.cumsum(storage)
    data = data/m
    
    return data
    

  
def numberOneD():
    start = timeit.default_timer()
    numberOneA(5000)
    stop = timeit.default_timer()
        
    time = (start - stop)
    print(time)

 
numberOneD()


def numberTwoA(count):
    present = True
    dict = {}
    result = 0;
    for i in range(0, count):
        dict[i] = rand.randint(0, 300)
        
    while(present):
        r = rand.randint(0, 300)
        if(len(dict) == 0):
            present = False
            break
                
        if(dict.__contains__(r)):
            dict.__delitem__(r)
        else:
            result = result + 1
            
    return result
    
numberTwoA(300)


#this is for number two of the problem

def numberTwoB():
    storage = np.zeros(5000)
    
    for i in range(0, 400):
        storage[numberTwoA(300)] += 1
        
    data = np.cumsum(storage)
    data = data/400
    
   
    plt.plot(data)
    plt.show