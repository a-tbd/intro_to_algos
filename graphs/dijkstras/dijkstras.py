'''
Coursera Dijkstra's Shortest path
'''

import csv
import collections

def load_graph(inp):
    ''' 
    '''
    with open(inp,'rb') as f:
            reader = csv.reader(f, delimiter='\t')
            num = list(reader)

    return {int(r[0]): 
            {tuple(map(int, t))[0]: 
             tuple(map(int, t))[1] for t in map(lambda x: tuple(x.split(',')), r[1:]) if len(t) > 1} 
             for r in num}

def dijkstras(graph, source):
    shortest_paths = {k: float('inf') for k in range(1,201)}
    shortest_paths[1] = 0
    stack = collections.deque([1])
    visited = set()
    
    while stack:
        node = stack.popleft()
        visited.add(node)
        for v in graph[node]:
            if not v in visited:
                stack.append(v)
            path = graph[node][v] + shortest_paths[node]
            if shortest_paths[v] > path:
                shortest_paths[v] = path
    return shortest_paths

shortest_paths = dijkstras(load_graph('dijkstras_data.csv'), 1)

vertices = [7,37,59,82,99,115,133,165,188,197]

for v in vertices:
    print shortest_paths[v]

