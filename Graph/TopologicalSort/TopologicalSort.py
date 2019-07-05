from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, parent, child):
        if type(child) == list:
            self.graph[parent].extend(child)
        else:
            self.graph[parent].append(child)

    def _top_sort_after(self, v, visit, stack):
        visit[v] = True

        for i in self.graph[v]:
            if(not visit[i]):
                self._top_sort_after(i, visit, stack)

        stack.append(v)

    def top_sort(self):
        visit = [False]*len(self.graph)
        stack = list()

        for i in self.graph.keys():
            if(not visit[i]):
                self._top_sort_after(i, visit, stack)

        return stack


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, [])
    graph.add_edge(1, [])
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.add_edge(4, [0, 1])
    graph.add_edge(5, [2, 0])
    print(*graph.top_sort()[::-1])
