import sys
import heapq
import queue as Queue

def main():
     pQ = readInput()
     while pQ.empty() is False:
        print("{0:.4f}".format(pQ.get()))
        
def readInput():
    pQ = Queue.Queue()
    line = sys.stdin.readline().split()
    n = int(line[0])
    m = int(line[1])
    
    while((n > 0) and (m > 0)):
        corridors = {}
        for i in range(0, n):
            corridors[i] = {}
            
        for i in range(0, m):
            corridor = sys.stdin.readline().split()
            first = int(corridor[0])        
            second = int(corridor[1])
            flo = float(corridor[2]) * -1
            if first == second:
                pass
            elif second in corridors[first] and corridors[first][second] < flo:
                pass
            else:
                corridors[second][first] = flo
                corridors[first][second] = flo
        endSize = round(abs(dijkstras(n, corridors)[n-1]),4)
        pQ.put(endSize)
        line = sys.stdin.readline().split()
        n = int(line[0])
        m = int(line[1])  
   
    return pQ;
        
def dijkstras(n, corridors):
    distance = [0] * n
    prev = [None] * n
    isVisited = [False] * n

    distance[0] = 1
    h = []
    heapq.heappush(h,(-1, 0))

    while len(h) > 0:
        popped = heapq.heappop(h)
        u = popped[1]
        isVisited[u] = True
        corridorDict = corridors[u]
        for v in corridorDict:
            w = corridorDict[v]
            if distance[v] < distance[u] * -w:
                distance[v] = float(distance[u] * -w)
                prev[v] = u
                if isVisited[v] == False:
                    heapq.heappush(h, (-distance[v], v))
    return distance

if __name__ == "__main__":
    main()
