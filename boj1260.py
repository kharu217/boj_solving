import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs_r(graph, start, visited = []) :
    visited.append(start)
    
    for node in graph[start] :
        if node not in visited :
            dfs_r(graph, node, visited)
    return visited

def bfs(graph, start_node) :
    need_visited, visited = [], []
    need_visited.append(start_node)
    
    while need_visited :
        node = need_visited[0]
        del need_visited[0]
        
        if node not in visited :
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

N, M, t = map(int, input().split())

graph = {i:[] for i in range(N)}
for i in range(M) :
    u, v = map(int, input().split())
    
    if u not in graph.keys() :
        graph[u] = []
    if v not in graph.keys() :
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)
    
    graph[u].sort()
    graph[v].sort()

print(*dfs_r(graph, t))
print(*bfs(graph, t))
