from queue import PriorityQueue

v = 14
graph = [[] for _ in range(v)]

def addedge(x,y,cost):
    graph[x].append((y,cost))
    graph[y].append((x,cost))

def bestFirstSearch(source,target,n):
    visited = [False]*n
    pq = PriorityQueue()
    pq.put((0,source))
    visited[source] = True
    
    while(pq.empty() == False):
        u = pq.get()[1]
        print(u, end=' ')
        if (u == target):
            break
        for v,c in graph[u]:
            if (visited[v] == False):
                visited[v] = True
                pq.put((c,v))
    print()

addedge(0,1,3)
addedge(0,2,6)
addedge(0,3,6)
addedge(1,4,1)
addedge(1,5,8)
addedge(2,6,12)
addedge(2,7,14)
addedge(3,8,2)
addedge(8,9,9)
addedge(8,10,6)
addedge(9,11,1)
addedge(9,12,10)
addedge(9,13,12)

source = 0
target = 9
bestFirstSearch(source,target,v)