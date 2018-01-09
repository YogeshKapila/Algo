"""
Breadth First Traversal for a Directed Graph.
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

    def bfs(self, start_node):
        visited = [False for _ in range(len(self.graph))]

        bfs_queue = list()
        bfs_queue.append(start_node)
        visited[start_node] = True

        while len(bfs_queue):
            elem = bfs_queue.pop(0)
            print(elem, end=' ')

            for node in self.graph[elem]:
                if not visited[node]:
                    bfs_queue.append(node)
                    visited[node] = True


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    graph.print_graph()

    graph.bfs(1)
