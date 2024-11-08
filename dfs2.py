class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    def dfs(self, start_node):
        visited = set()
        self._dfs_util(start_node, visited)
        return visited
    def _dfs_util(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs_util(neighbor, visited)

g = Graph()
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    u, v = map(int, input("Enter an edge (u,v): ").split())
    g.add_edge(u, v)
start_node = int(input("Enter the starting node for DFS Traversal: "))
print("DFS Traversal starting from node", start_node, ":")
g.dfs(start_node)