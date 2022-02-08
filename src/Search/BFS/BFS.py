graph = {'A':['B','C'],
         'B':['D','A'],
         'D':['B','C'],
         'C':['D','E','A'],
         'E':['D','C','F'],
         'F':['E']}


def findMinDistPath(graph, start, end):
    q = [[start, [start]]]
    visited = {start}
    
    while q:
        node, path = q.pop(0)
        for neighbor in graph[node]:
            if not neighbor in visited:
                if neighbor == end:
                    return path + [neighbor]
                visited.add(neighbor)
                q.append([neighbor, path + [neighbor]])

    
    return []

def findAllPaths(graph, start, end):
    all_paths = []
    q = [[start, [start]]]
    visited = {start}

    while q:
        node, path = q.pop(0)
        for neighbor in graph[node]:
            if not neighbor in visited:
                visited.add(neighbor)
                q.append([neighbor, path+[neighbor]])
                if neighbor == end:
                    all_paths.append(path+[neighbor])
                visited.remove(neighbor)
    
    for path in all_paths:
        print(path)


path = findMinDistPath(graph, 'A', 'F')
print(path)

findAllPaths(graph, 'A', 'F')