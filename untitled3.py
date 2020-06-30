#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:03:57 2019

@author: riteshsharma
"""
import sys


#this method calculates the distance between stars (x1-x2)^2 + (y1-y2)^2
def distance(star1, star2):
    x1 = int(star1[0])
    y1 = int(star1[1])
    
    x2 = int(star2[0])
    y2 = int(star2[1])
    
    result = ((x1 - x2) * (x1 - x2)) + ((y1- y2) * (y1 - y2))
    return result
    
#this method finds the majority by keeping diameter as a constraint.
def findMajority(galaxy, d):
    x = list()
    y = list()
    galaxyList = list()
    
    if(len(galaxy) == 0):
        return None
        
    elif(len(galaxy) == 1):
        return (galaxy[0])

    else:
        i = 0
        while(i < len(galaxy)):
            if(i < (len(galaxy) - 1)):
                if(distance(galaxy[i] , galaxy[i+1]) <= d):
                    galaxyList.append(galaxy[i])
            else:
                y = galaxy[i]
            i = i + 2
            
        x = findMajority(galaxyList, d)
        
        if(x == 0):
            if(not len(galaxy) % 2 == 0):
                count = 0
                
                for arr in galaxy:
                    if(distance(y, arr) <= d):
                        count = count + 1
                        
                if(count > (len(galaxy)/2)):
                    y.append(count)
                    return y
                else:
                    return None
                    
            else:
                return None
                
        else:
            count = 0
            for arr in galaxy:
                if(distance(x, arr) <= d):
                    count = count + 1
                    
            if(count > (len(galaxy)/2)):
                x.append(count)
                return x
                
            else:
                return None
                

def main():
    d = 0
    boolean = False
    starList = list()
    #data = "20 7\n2 2\n3 2\n1 1\n1 2\n1 3\n101 101\n100 100\n102 102\n3 3"
    #for line in data.split('\n'):
    for line in sys.stdin.read().split('\n'):
        if not line:
            continue
        
        if not boolean:
            temp = list()
            temp = line.split()
            d = int(temp[0])
            d = d * d
            
            boolean = True
        else:
            star = list()
            temp = list()
            temp = line.split()
            star.append(temp[0])
            star.append(temp[1])
            starList.append(star)
    output = findMajority(starList, d)
    if(output == None):
        print("NO")
    else:
        print(output.pop())

main()
    
   

