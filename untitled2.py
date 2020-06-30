#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:58:44 2019

@author: riteshsharma
"""
import bcrypt as bc
import hashlib
import numpy as np
import matplotlib.pyplot as plt
import time

def numberTwo(t):
    F1 = open("D1.txt", "r")
    F2 = open("D2.txt", "r")
    
    
    data1 = F1.readlines()
    data2 = F2.readlines()
     
    wholeString1 = list()
    wholeString2 = list()
    
    kGramsStorage1 = set()
    kGramsStorage2 = set()
    
    for text1 in data1:
        wholeString1 += text1
        
    for text2 in data2:
        wholeString2 += text2
    

    for j in range(0, len(wholeString1) - 2):
        kGramsStorage1.add(wholeString1[j] + wholeString1[j+1] + wholeString1[j+2])
    
    for k in range(0, len(wholeString2) - 2):
        kGramsStorage2.add(wholeString2[k] + wholeString2[k+1] + wholeString2[k+2])
    
    
    #Fast Min Hash Algorithm
    


    salt = list()
    vector = list()
    
    for i in range(t):
        vector.append(np.Inf)
    
    def sha(salt, value):
        hashValue = hashlib.sha1(salt.encode() + value.encode()).hexdigest()
        return int(hashValue, 16) % 10_000
        

    for i in range(t):
        salt.append(str(bc.gensalt()))
    
    for kGram in kGramsStorage1:
        for i in range(t):
            if (sha(salt[i], kGram) < vector[i]):
                vector[i] = sha(salt[i], kGram)
                
    jaccardSimilaritya = 0
    
    ##vector2
    vector1 = list()
    
    for i1 in range(t):
        vector1.append(np.Inf)
        

    for kGram in kGramsStorage2:
        for i1 in range(t):
            if (sha(salt[i1], kGram) < vector1[i1]):
                vector1[i1] = sha(salt[i1], kGram)
                
    
    for i in range(t):
        if(vector[i] == vector1[i]):
            jaccardSimilaritya += 1
            
    jaccardSimilaritya = jaccardSimilaritya/t
    
    return jaccardSimilaritya
    
    
def graph():
    a = list()
    ti = list()
    
    for i in range(20, 1000, 20):
        start = time.clock()
        a.append(numberTwo(i))
        stop = time.clock()
        b = stop - start
        ti.append(b)
    
    

    plt.plot(ti)
    plt.ylabel("time")
    plt.xlabel("t")
    plt.show
    
graph()
