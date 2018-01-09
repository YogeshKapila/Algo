"""
Depth First Traversal for a Directed Graph.
"""

from collections import defaultdict


class Graph:
    """
    Adjacency List representation of Graph with helper functions.
    """
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def print_graph(self):
        for key, value in self.graph.items():
            print(key, "->", value)

    def dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=' ')
        for node in self.graph[vertex]:
            if not visited[node]:
                self.dfs_util(node, visited)

    def dfs(self):
        visited = [False for _ in range(len(self.graph))]

        for key in self.graph.keys():
            if not visited[key]:
                self.dfs_util(key, visited)


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    graph.print_graph()

    graph.dfs()
