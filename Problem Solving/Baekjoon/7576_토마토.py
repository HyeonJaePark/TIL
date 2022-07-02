import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
box = [
    list(map(int, input().split()))
    for _ in range(n)
]
total_tomato = sum(x.count(1) + x.count(0) for x in box)
cnt_tomato = 0
answer = 0

dxs = [-1, 1, 0, 0] # 상하좌우
dys = [0, 0, -1, 1]

def box_boundary(x, y):
    return True if (((0 <= x) and (x < n)) and ((0 <= y) and (y < m))) else False

def is_tomato(x, y):
    return True if box[x][y] == 0 else False

d = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            d.append((i, j, 0)) # i, j, day
            cnt_tomato += 1

while True:
    if cnt_tomato == total_tomato:
        print(answer)
        break
    if len(d) == 0 and cnt_tomato != total_tomato:
        print(-1)
        break
    x, y, day = d.popleft()
    for i in range(4):
        if box_boundary(x + dxs[i], y + dys[i]) == True:
            if is_tomato(x + dxs[i], y + dys[i]) == True:
                box[x + dxs[i]][y + dys[i]] = 1
                cnt_tomato += 1
                d.append((x + dxs[i], y + dys[i], day + 1))
                answer = day + 1