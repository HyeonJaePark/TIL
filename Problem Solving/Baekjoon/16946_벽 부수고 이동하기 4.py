def inbound(r, c):
    global n, m
    return True if (0 <= r < n) and (0 <= c < m) and worldmap[r][c] != 1 else False


def bfs(r, c, sepcnt):
    cnt = 1
    d = deque([(r, c)])
    worldmap[r][c] = sepcnt
    

    while d:
        cr, cc = d.popleft()
        for i in range(4):
            nr = cr + dxs[i]
            nc = cc + dys[i]
            if inbound(nr, nc):
                if worldmap[nr][nc] == 0:
                    d.append((nr, nc))
                    cnt += 1
                    worldmap[nr][nc] = sepcnt
    
    count[sepcnt] = cnt
    
                    
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
worldmap = [
    [] for _ in range(n)
]
for _ in range(n):
    worldmap[_] = list(map(int, input().rstrip()))
count = {}
answer = [
    [0 for _ in range(m)]
    for _ in range(n)
]
sepcnt = 2
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if worldmap[i][j] == 0:
            bfs(i, j, sepcnt)
            sepcnt += 1

for i in range(n):
    for j in range(m):
        if worldmap[i][j] == 1:
            visited = set()
            for k in range(4):
                ni = i + dxs[k]
                nj = j + dys[k]
                if inbound(ni, nj):
                    visited.add(worldmap[ni][nj])
            for visit in visited:
                answer[i][j] += count[visit]
            answer[i][j] = (answer[i][j] + 1) % 10

for i in answer:
    print(''.join(list(map(str, i))))