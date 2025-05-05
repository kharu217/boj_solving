import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs_r(graph, start, visited=[]) :
    visited[start] = True
    
    for i in graph[start] :
        if not visited[i] :
            dfs_r(graph, i, visited)
    return visited

N = int(input())
M = int(input())
graph = {i:[] for i in range(1, N + 1)}
visited = [False for _ in range(N+1)]

for node in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
print(dfs_r(graph, 1, visited).count(True) - 1)
