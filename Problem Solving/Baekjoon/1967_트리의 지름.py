import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def dfs(cur_node, weight):
    for node, cost in tree[cur_node]:
        if distances[node] == -1:
            distances[node] = weight + cost
            dfs(node, weight + cost)


n = int(input())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    tree[a].append([b, c])
    tree[b].append([a, c])

distances = [-1 for _ in range(n + 1)]
distances[0] = 0
dfs(1, 0)

start = distances.index(max(distances))
distances = [-1 for _ in range(n + 1)]
distances[start] = 0
dfs(start, 0)

print(max(distances))
