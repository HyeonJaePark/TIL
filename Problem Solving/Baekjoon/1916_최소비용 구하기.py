import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
costs = defaultdict(dict)
visited = [sys.maxsize for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    try:
        i = costs[s][e]
    except KeyError:
        costs[s].update({e: c})
    else:
        if c < i:
            costs[s][e] = c
start, dest = map(int, input().split())
print(costs)
d = deque([start])
visited[start] = 0
while d:
    c = d.popleft()
    p = visited[c]
    for nc in costs[c]:
        np = p + costs[c][nc]
        if visited[nc] > np:
            visited[nc] = np
            if nc != c:
                d.append(nc)
print(visited[dest])