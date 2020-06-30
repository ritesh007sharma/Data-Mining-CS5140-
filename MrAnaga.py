
import random as rand
import string
import time
import matplotlib.pyplot as plt



def generateRandom(n, k):
    uniqueWords = set()
    while(len(uniqueWords) <= n):
        rr = ''.join([rand.choice(string.ascii_letters).lower() for n in range(k)])
        uniqueWords.add(rr)
     
    return uniqueWords



def MrAnaga(data):
    
    #dict that contains solutions
    solutions = dict()
    #set that stores rejected values.
    rejected = set()
    #for loop to read from the input.
    for word in data:
        
        #algorithm to figure out anagramars
        sortedWord = ''.join(sorted(word))
        if(sortedWord in solutions):
            solutions.pop(sortedWord)
            rejected.add(sortedWord)
        elif not (sortedWord in rejected):
            solutions[sortedWord] = word
        
    #return len(solutions)

    
    
    
def timingExperiment():
    list = []
   
    k = 5
    klist =[]
    average = 0
    total = 0
    
    
    while(k <= 800):
        data = generateRandom(2000 , k)
      
        start = time.clock()
        for i in range(20):
            
            MrAnaga(data)
        stop = time.clock()
            
        total = total + (stop - start)
            
        average = total/20
        print(average)
        
        
   
        list.append(average)
        k = k * 2
        klist.append(k)
    
    plt.plot(klist,list)
    plt.show
    
        

timingExperiment()   



    


    
