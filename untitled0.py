#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 01:10:55 2019

@author: riteshsharma
"""
import sys
from llist import dllist

Cities = dict()
al = dict()
sort = list()
count = 0

class City:
    
    def __init__(self):
        self.Name = ""
        self.Price = 0
        self.pre = 0
        self.post= 0
        self.isVisited = False
        self.previous = None
        self.cost = sys.maxsize
        
class Edge:
    def __init__(self):
        self.dest = City()
    

class AutoSink:
    
    def dfs(a):
        global count
        Cities[a].isVisited = True
        Cities[a].pre = count + 1
        
        if(not al[a] == None):
            for e in al[a]:
                if(not e.dest.isVisited):
                    AutoSink.dfs(e.dest.Name)
            Cities[a].post = count + 1
            sort.append(Cities[a])
    
    def toposort(str):
        
        for c in Cities.values():
            if(not c.isVisited):
                AutoSink.dfs(c.Name)
    
    
    def cheapestPath(start, end):
         a = sys.maxsize
         for c in Cities.values:
             c.cost= a
             c.previous = None
             
         s = list()
         
         for b in sort:
             s.append(b)
        
         startingCity = Cities[start]
         startingCity.cost = 0;
         
         while(not s.count == 0):
             city = s.pop()
             if((not city.cost == a) and (not al[city.Name] == None)):
                 for edge in al[city.Name]:
                     key = edge.dest.Name
                     if(Cities[key].cost > city.cost + Cities[key].Price):
                         Cities[key].cost = city.cost + Cities[key].Price
             
    
    def tripCalculation(count, send):
        results = list()
        result = 0
        
        AutoSink.toposort(Cities[send].Name)
        read2 = "Sourceville SinkCity\nEaston SinkCity\nSinkCity SinkCity\nWeston Weston\nWeston Sourceville\nSinkCity Sourceville"
        for i in range(0, count):
            
            read = read2.split("\n")#sys.stdin.readline()
            path = read.split(" ")
            startingPoint = path[0]
            endingPoint = path[1]
            
            if(startingPoint == endingPoint):
                result = "0"
            else:
                AutoSink.cheapestPath(startingPoint, endingPoint)
                a = Cities[endingPoint]
                
                if(a.cost == sys.maxsize):
                    result = "NO"
                else:
                    result = str(a.cost)
            results.append(result)
        for i in results:
            print(i)
    
    
    
    def main():
        numberOfCities = 4#int(sys.stdin.readline())
        nameAndPrice2 = "SourceVille 5\nSinkCity 10\nEaston 20\nWeston 15"
        for i in range(0, numberOfCities):
            nameAndPrice = nameAndPrice2.split('\n')#sys.stdin.readline()
            arr = nameAndPrice[i].split(" ")
            
            City.Name = arr[0]
            if(i == 0):
                send = arr[0]
            City.Price = int(arr[1])
            Cities[City.Name] = City
            al[City.Name] = None
            
        hwAndEdges = 4#int(sys.stdin.readline())
        
        connection2 =  "SourceVille Easton\nSourceVille Weston\nWeston SinkCity\nWeston SinkCity"
        for j in range(0, hwAndEdges):
            connection = connection2.split("\n")#sys.stdin.readline()
   
            arrTwo = connection[j].split(" ")
            edge = Edge.dest = Cities[arrTwo[1]]
            if(al[arrTwo[0]] is None):
                a = dllist()
                a.appendleft(edge)
                
                al[arrTwo[0]] = a
            else:
                al[arrTwo[0]].appendright(edge)
                
        numberOfComputation = 6#int(sys.stdin.readline())
        AutoSink.tripCalculation(numberOfComputation, send)
        
    
            
        

AutoSink.main()     
        