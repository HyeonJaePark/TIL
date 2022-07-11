from collections import deque
import sys

dice = [x for x in range(1, 7)]
visited = [sys.maxsize for _ in range(101)]
ladders = {}
snakes = {}

n, m = map(int, input().split())
for _ in range(n):
    s, e = map(int, input().split())
    ladders[s] = e
for _ in range(m):
    s, e = map(int, input().split())
    snakes[s] = e

d = deque([1])
visited[1] = 0

while d:
    x = d.popleft()
    cnt = visited[x]
    for i in dice:
        nx = x + i
        if nx <= 100:
            if nx in ladders:
                if visited[nx] > cnt + 1:
                    visited[nx] = cnt + 1
                    mx = ladders[nx]
                    if visited[mx] > cnt + 1:
                        visited[mx] = cnt + 1
                        d.append(mx)
            elif nx in snakes:
                if visited[nx] > cnt + 1:
                    visited[nx] = cnt + 1
                    mx = snakes[nx]
                    if visited[mx] > cnt + 1:
                        visited[mx] = cnt + 1
                        d.append(mx)
            else:
                if visited[nx] >= cnt + 1:
                    d.append(nx)
                    visited[nx] = cnt + 1
print(visited[100])