v = int(input("Enter no.of vertices: "))
print("Enter adjacency matrix for a graph: ")
graph = [list(map(int,input().split())) for i in range(v)]
def isValid(v, color, c): 
    for i in range(v):
        if graph[v][i] and c == color[i]:
            return False
    return True
def mColoring(colors, color, vertex):
    if vertex == v:  
        return True
    for col in range(1, colors + 1):
        if isValid(vertex, color, col):  
            color[vertex] = col
            if mColoring(colors, color, vertex + 1):
                return True 
            color[vertex] = 0
    return False
colors = v-1  
color = [0] * v
if not mColoring(colors, color, 0): 
    print("Solution does not exist.")
else:
    print("Assigned Colors are:")
    for i in range(v):
        print("Vertex",i+1,"->",color[i])