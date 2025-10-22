import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class GraphStructure:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                queue.extend(self.graph[node])

        print("BFS:", result)
        return result

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_recursive(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.graph[node]:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        print("DFS:", result)
        return result

    def show_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

    def draw(self):
        G = nx.Graph()
        for node in self.graph:
            for neighbor in self.graph[node]:
                G.add_edge(node, neighbor)

        nx.draw(G, with_labels=True, node_color='skyblue', node_size=800, font_weight='bold')
        plt.show()

if __name__ == "__main__":
    g = GraphStructure()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('D', 'F')

    print("Graph Structure:")
    g.show_graph()

    g.bfs('A')
    g.dfs('A')

    g.draw()
