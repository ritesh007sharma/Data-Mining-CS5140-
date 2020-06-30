
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
    data1 = F1.read().split()
    data2 = F2.read().split()
    data3 = F3.read().split()
    data4 = F4.read().split()
    
    wholeString1 = list()
    wholeString2 = list()
    wholeString3 = list()
    wholeString4 = list()
  

    kGramsStorage1 = set()
    kGramsStorage2 = set()
    kGramsStorage3 = set()
    kGramsStorage4 = set()
    

    for a in data1:
        wholeString1.append(a)
        
    for b in data2:
        wholeString2.append(b)
        
    for c in data3:
        wholeString3.append(c)
        
    for d in data4:
        wholeString4.append(d)
    
    for i in range(len(wholeString1) - 1):
        kGramsStorage1.add(wholeString1[i] + wholeString1[i+1])
    print(len(kGramsStorage1))
    
    for j in range(len(wholeString2) - 1):
        kGramsStorage2.add(wholeString2[j] + wholeString2[j+1])
    print(len(kGramsStorage2))
        
    for k in range(len(wholeString3) - 1):
        kGramsStorage3.add(wholeString3[k] + wholeString3[k+1])
    print(len(kGramsStorage3))
        
    for l in range(len(wholeString4) - 1):
        kGramsStorage4.add(wholeString4[l] + wholeString4[l+1])
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
    print(jaccardSimilarity)           
        
    
twoGramsCharacter()
        
        
    
   
twoGramsCharacter()