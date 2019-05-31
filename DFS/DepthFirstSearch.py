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

    def dfs(self, start,visited=None):
        if visited == None:
            visited = [False]*(1+len(self.graph))
            visited[0] = None   # Not using the first Index

        visited[start] = True
        print(start,end=' ')

        for node in self.graph[start]:
            if not visited[node]:
                self.dfs(node,visited)



def main():
    graph = Graph()

    graph.add_edge(1, [2, 3])
    graph.add_edge(2, [1, 4, 5])
    graph.add_edge(3, [1, 5])
    graph.add_edge(4, [2, 5, 6])
    graph.add_edge(5, [2, 3, 4, 6])
    graph.add_edge(6, [4, 5])

    print('DFS of the Graph is\n')
    graph.dfs(1)


if __name__ == "__main__":
    main()
