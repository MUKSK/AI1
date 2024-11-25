import heapq
def astar(graph,h,goal,start):
    o=[]
    gcost={start:0}
    parent={start:None}
    heapq.heappush(o,(h[start],start))
    while o:
        _,current_node=heapq.heappop(o)
        if current_node==goal:
            path=[]
            while current_node is not None:
                path.append(current_node)
                current_node=parent[current_node]
            return path[::-1]
        for n,cost in graph[current_node].items():
            tg=gcost[current_node]+cost
            if n not in gcost or tg<gcost[n]:
                gcost[n]=tg
                fcost=tg+h[n]
                parent[n]=current_node
                heapq.heappush(o,(fcost,n))
    return None
def ans():
    graph={}
    h={}
    nn=int(input("Enter number of nodes"))
    for _ in range(nn):
        node=input("Enter node name").strip()
        graph[node]={}
        nnum=int(input("Enter number of nieghbours"))
        for _ in range(nnum):
            neighbour,cost=input("Enter both").split()
            graph[node][neighbour]=int(cost)
    print("Heuristic values")
    for node in graph:
        h[node]=int(input(f"Enter value for {node}"))
    start=input("Start").strip()
    goal=input("goal").strip()
    return graph,h,start,goal
graph,h,start,goal=ans()
path=astar(graph,h,goal,start)
if(path):
    print(f"path is:{'->'.join(path)}")
else:
    print("Path  not found")
