from collections import defaultdict
import sys


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, parent, child):
        if type(child) == list:
            self.graph[parent].extend(child)
        else:
            self.graph[parent].append(child)

    def min_distance(self, distance, visited):
        m = sys.maxsize
        idx = None
        for i in range(len(distance)):
            if(distance[i] < m and not visited[i]):
                m = distance[i]
                idx = i
        return idx

    def dijkstras(self, start):
        distance = [sys.maxsize]*len(self.graph)
        distance[start] = 0
        visited = [False]*len(self.graph)

        for _ in range(len(self.graph)):
            u = self.min_distance(distance, visited)

            visited[u] = True

            for ni, dis in self.graph[u]:
                if(not visited[ni]):
                    distance[ni] = min(
                        distance[ni],
                        distance[u]+dis)

        return distance


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, [(1, 4), (7, 8)])
    graph.add_edge(1, [(0, 4), (2, 8), (7, 11)])
    graph.add_edge(2, [(1, 8), (3, 7), (5, 4), (8, 2)])
    graph.add_edge(3, [(2, 7), (4, 9), (5, 14)])
    graph.add_edge(4, [(3, 9), (5, 10)])
    graph.add_edge(5, [(2, 4), (3, 14), (4, 10), (6, 2)])
    graph.add_edge(6, [(5, 2), (7, 1), (8, 6)])
    graph.add_edge(7, [(0, 8), (1, 11), (6, 1), (8, 7)])
    graph.add_edge(8, [(2, 2), (6, 6), (7, 7)])

    distance = graph.dijkstras(0)
    print('Vertex\tDistance')
    for node, dis in enumerate(distance):
        print(f'{node}\t{dis}')
