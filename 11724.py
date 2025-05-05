import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs_r(graph, v, visited) :
    visited[v] = True
    for i in graph[v] :
        if not visited[i] :
            dfs_r(graph, i, visited)

N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
visited = [False] * (N + 1)

#하나의 노드를 타고 연결된 다른 노드를 모두 탐색하여
#연결된 하나의 구역이 전부 True로 바뀜 -> 함수 한번에 연결 요소 하나 탐색색
for i in range(1, N+1):
    if not visited[i] :
        dfs_r(graph, i, visited)
        count += 1
print(count)
