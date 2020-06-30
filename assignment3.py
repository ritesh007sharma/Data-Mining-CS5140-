#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:25:26 2019

@author: riteshsharma
"""
##Construction for 2 grams based on character.
def twoGramsCharacter():
    F1 = open("D1.txt", "r")
    F2 = open("D2.txt", "r")
    F3 = open("D3.txt", "r")
    F4 = open("D4.txt", "r")
    data1 = F1.readlines()
    data2 = F2.readlines()
    data3 = F3.readlines()
    data4 = F4.readlines()
    
    wholeString1 = list()
    wholeString2 = list()
    wholeString3 = list()
    wholeString4 = list()
    kGramsStorage1 = set()
    kGramsStorage2 = set()
    kGramsStorage3 = set()
    kGramsStorage4 = set()
    for text1 in data1:
        wholeString1.append(text1)
        
    for text2 in data2:
        wholeString2.append(text2)
        
    for text3 in data3:
        wholeString3.append(text3)
        
    for text4 in data4:
        wholeString4.append(text4)
        
        
    for i in wholeString1.split("\n"):
        print()
    print(len(kGramsStorage1))
    
    for j in range(0, len(wholeString2) - 2):
        kGramsStorage2.add(wholeString2[j] + wholeString2[j+1] + wholeString2[j+2])
    print(len(kGramsStorage2))
    
    for k in range(0, len(wholeString3) - 2):
        kGramsStorage3.add(wholeString3[k] + wholeString3[k+1] + wholeString3[k+2])
    print(len(kGramsStorage3))
    
    for l in range(0, len(wholeString4) - 2):
        kGramsStorage4.add(wholeString4[l] + wholeString4[l+1] + wholeString4[l+2])
    print(len(kGramsStorage4))

    
    jaccardSimilarity1 = set()
    jaccardSimilarity2 = set()
    a = list(kGramsStorage3)
    b = list(kGramsStorage4)
    mergedSet= a + b
    for c in mergedSet:
        jaccardSimilarity1.add(c)

    
    
    for d in kGramsStorage3:
        if kGramsStorage4.__contains__(d):
            jaccardSimilarity2.add(d)
            
    jaccardSimilarity = len(jaccardSimilarity2)/len(jaccardSimilarity1)
    #print(jaccardSimilarity)           
        
    
twoGramsCharacter()
    
