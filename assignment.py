#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 12:19:22 2019

@author: riteshsharma
"""
import numpy as np
import urllib.request
import matplotlib.pyplot as plt
from numpy import random, sqrt, log, sin, cos, pi
from sklearn.preprocessing import normalize
from pylab import show,hist,subplot,figure
from scipy.stats import norm


def questionA(s,r, b):
   
    
    f = 1 - (1- s**b)**r
    
    plt.plot(f)
    plt.show
    
    
#questionA(0.85, 16, 10)



def questionB():
    a = [0.75, 0.25,0.35, 0.1, 0.45, 0.92]
    for i in a:
        result = questionA(i, 16, 10)
        print(result)
#questionB()

def boxMuller(u1,u2):
  z1 = sqrt(-2*log(u1))*cos(2*pi*u2)
  z2 = sqrt(-2*log(u1))*sin(2*pi*u2)
  return z1,z2 

def normalize(v):
  
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm   



def gaussianDistribution():
    
    
    data = np.zeros(100)
    g = list()
    d= list()
    #for i in range(80):
    for i in range(100):     
        a = random.uniform(0,1)
        u1 = np.array(a)
        b = random.uniform(0,1)
        u2 = np.array(b)
     
        
    data = boxMuller(u1, u2)
    
    return data

  
    
def unitVector():
    arr = list()
  
    for i in range(80):
        data = gaussianDistribution()
        arr.append(data)

        
        

    unit = normalize(arr)
  
    return unit


def numberOneB(n, m):
  
    storage = np.zeros(m)
   
    for i in range(0, m):
        storage[numberOneA(n)] +=  1

    
    data = np.cumsum(storage)
    data = data/m
    
    return data


def pairWiseDot():
    p = list()
    
    r = unitVector()
    storage = np.zeros(100)
   
    for i in range(0, len(r)):
        for j in range(i, len(r)-1):
            data = np.dot(r[i], r[j])
            p.append(data)
            
       
  
    return p
    

    
data= pairWiseDot()
plt.title("3A")
plt.ylabel("n")
plt.xlabel("n by two values")
plt.plot(data)
plt.show
        
    

