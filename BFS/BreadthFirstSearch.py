# Time Complexity - O(V)    V= Nodes in graph
# Space Complexity - O(V)


from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, parent, child):
        if type(child) == list:
            self.graph[parent].extend(child)
        else:
            self.graph[parent].append(child)

    def bfs(self, start):
        visited = [False]*(1+len(self.graph))
        visited[0] = None   # Not using the first Index

        queue = list()
        queue.append(start)

        while queue:
            current_node = queue.pop(0)
            print(current_node, end=' ')
            visited[current_node] = True

            explore_nodes = self.graph[current_node]
            for node in explore_nodes:
                if (not visited[node]) and (node not in queue):
                    queue.append(node)


def main():
    graph = Graph()

    graph.add_edge(1, [2, 3])
    graph.add_edge(2, [1, 4, 5])
    graph.add_edge(3, [1, 5])
    graph.add_edge(4, [2, 5, 6])
    graph.add_edge(5, [2, 3, 4, 6])
    graph.add_edge(6, [4, 5])

    print('BFS of the Graph is\n')
    graph.bfs(1)


if __name__ == "__main__":
    main()
