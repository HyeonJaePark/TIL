import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
nodes = defaultdict(list)
for _ in range(m):
    x, y = map(int, input().split())
    nodes[x].append(y)
    nodes[y].append(x)
for node in nodes:
    nodes[node].sort()

# DFS
visited = [False for _ in range(n + 1)]
dfs_history = []
def dfs(curr_node):
    visited[curr_node] = True
    dfs_history.append(curr_node)
    for node in nodes[curr_node]:
        if visited[node] == False:
            dfs(node)
    return
        
dfs(v)
print(str(dfs_history)[1:-1].replace(',', ''))

# BFS
visited = [False for _ in range(n + 1)]
bfs_history = []
d = deque()
d.append(v)
visited[v] = True
while True:
    if len(d) == 0:
        print(str(bfs_history)[1:-1].replace(',', ''))
        break
    curr_node = d.popleft()
    bfs_history.append(curr_node)
    for node in nodes[curr_node]:
        if visited[node] == False:
            d.append(node)
            visited[node] = True
    