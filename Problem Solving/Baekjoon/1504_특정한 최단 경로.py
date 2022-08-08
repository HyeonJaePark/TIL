from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def djikstra(start, dest):
    visited = [sys.maxsize for _ in range(n + 1)]
    d = deque([start])
    visited[start] = 0
    while d:
        x = d.popleft()
        c = visited[x]
        for nx in costs[x]:
            nc = c + costs[x][nx]
            if visited[nx] > nc:
                visited[nx] = nc
                if nx != dest:
                    d.append(nx)
    return visited[dest]

n, e = map(int, input().split())
costs = defaultdict(dict)
for _ in range(e):
    a, b, c = map(int, input().split())
    try:
        i = costs[a][b]
    except KeyError:
        costs[a].update({b: c})
        costs[b].update({a: c})
    else:
        if c < i:
            costs[a][b] = c
            costs[b][a] = c
v1, v2 = map(int, input().split())


# 1 to v2, v2 to v1, v1 to n
# 1 to v1, v1 to v2, v2 to n
s2v1 = djikstra(1, v1)
s2v2 = djikstra(1, v2)
v12v2 = djikstra(v1, v2)
v12n = djikstra(v1, n)
v22n = djikstra(v2, n)

answer = min(s2v1 + v12v2 + v22n, s2v2 + v12v2 + v12n)
if answer >= sys.maxsize:
    print(-1)
else:
    print(answer)