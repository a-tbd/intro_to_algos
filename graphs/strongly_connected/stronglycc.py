'''
Coursera intro to algorithms: graphs
Find the strongly connected components of a directed graph

'''
import csv
import collections
import pdb

class Graph(object):
    def __init__(self):
        self.graph = collections.defaultdict(lambda: [])
        self.rev_graph = collections.defaultdict(lambda: [])

    def set_graph(self, pairs):
        for n in pairs:
            n1, n2 = int(n[0]), int(n[1])
            self.graph.setdefault(n1, []).append(n2)
            self.rev_graph.setdefault(n2, []).append(n1)

    def topological_sort(self, graph):
        last_vertex = None
        dfs = DFS(len(graph))
        sorted_list = []
        # pdb.set_trace()
        for v in range(len(self.graph), 0, -1):
            if not v in dfs.visited:
            	dfs.stack = [v]
                last_vertex = v
                dfs.search(graph, v, last_vertex)
        return dfs.sort

    def find_leaders(self, graph, sort):
        last_vertex = None
        dfs = DFS(len(graph))
        while sort:
            v = sort.pop()
            if not v in dfs.visited:
                dfs.stack = [v]
                last_vertex = v
                dfs.search(graph, v, last_vertex)
        if min(dfs.top_sort) < dfs.leader[1]:
            index = dfs.top_sort.index(min(dfs.top_sort))
            dfs.top_sort[index] = dfs.leader[1]
        return dfs.top_sort


class DFS(object):
    def __init__(self, start_label, visited=None, sort=None, leaders=None):
        self.current_label = start_label
        self.visited = visited or set()
        self.stack = []
        self.sort = sort or []
        self.leaders = []
        self.leader = None
        self.top_sort = [0,0,0,0,0]

    def search(self, G, s, last_vertex):
        self.visited.add(s)
        temp_stack = []
        while self.stack:
            node = self.stack.pop()
            prev_len = len(self.stack)
            self.add_leaders(node, last_vertex)
            children = reversed(G[node])
            for e in children:
                #pdb.set_trace()
                if not e in self.visited and not e in self.stack:
                    self.stack.append(e)
                    self.visited.add(e)
            temp_stack.append(node)
        self.sort.extend(reversed(temp_stack))

    def add_leaders(self, s, last_vertex):
        if not self.leader:
            self.leader = [last_vertex, 1]
        elif self.leader[0] == last_vertex:
            self.leader[1] += 1
        elif self.leader[0] != last_vertex:
            if min(self.top_sort) < self.leader[1]:
                index = self.top_sort.index(min(self.top_sort))
                self.top_sort[index] = self.leader[1]
            self.leader = [last_vertex, 1]
        # self.leaders.append((s, last_vertex))


tests = ['testscc.csv', 'test2scc.csv', 'test3scc.csv', 'test4scc.csv', 'test5scc.csv', 'test6scc.csv']


def find_scc(graph_file):
    with open(graph_file,'rb') as f:
        reader = csv.reader(f, delimiter=" ")
        num = list(reader)
    graph = Graph()
    graph.set_graph(num)
    sorted_graph = graph.topological_sort(graph.rev_graph)
    print sorted_graph
    leaders = graph.find_leaders(graph.graph, sorted_graph)
    return sorted(leaders, reverse=True)

for t in tests:
    print find_scc(t)