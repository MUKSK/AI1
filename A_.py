import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h
   
    def __lt__(self, other):
        return self.f < other.f

def a_star_search(start, goal, graph, heuristic):
    open_set = []
    closed_set = set()
    start_node = Node(start, g=0, h=heuristic.get(start, 0))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.name == goal:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.name)

        for neighbor, cost in graph.get(current_node.name, []):
            if neighbor in closed_set:
                continue
            g_score = current_node.g + cost
            h_score = heuristic.get(neighbor, 0)
            neighbor_node = Node(neighbor, parent=current_node, g=g_score, h=h_score)

            for open_node in open_set:
                if open_node.name == neighbor and open_node.g <= g_score:
                    break
            else:
                heapq.heappush(open_set, neighbor_node)

    return None

graph = {}
print("Enter the graph edges and cost, type 'done' to finish:")
while True:
    edge = input()
    if edge.lower() == 'done':
        break
    try:
        node1, node2, cost = edge.split()
        cost = int(cost)
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append((node2, cost))
        graph[node2].append((node1, cost))  
    except ValueError:
        print("Invalid input format. Please enter in format 'A B 1'.")

heuristic = {}
print("Enter heuristic values, type 'done' to finish:")
while True:
    heuristic_input = input()
    if heuristic_input.lower() == 'done':
        break
    try:
        node, h_value = heuristic_input.split()
        heuristic[node] = int(h_value)
    except ValueError:
        print("Invalid input format. Please enter in format 'A 7'.")

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")
path = a_star_search(start_node, goal_node, graph, heuristic)

if path:
    print("Path found:", path)
else:
    print("Path not found.")