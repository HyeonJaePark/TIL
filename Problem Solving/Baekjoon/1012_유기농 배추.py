import sys
from collections import deque

input = sys.stdin.readline

def worldmap_boundary(y, x):
    return True if ((y >= 0) and (y < n) and (x >= 0) and (x < m)) else False

T = int(input())

for _ in range(T):
    answer = 0
    dxs = [0, 0, -1, 1] # 상하좌우
    dys = [-1, 1, 0, 0]
    m, n, k = map(int, input().split())
    worldmap = [
        [0 for _ in range(m)]
        for _ in range(n)
    ]
    visited = [
        [True for _ in range(m)]
        for _ in range(n)
    ]
    for _ in range(k):
        x, y = map(int, input().split())
        worldmap[y][x] = 1
        visited[y][x] = False
    d = deque()

    for y in range(n):
        for x in range(m):
            if visited[y][x] == False:
                d.append((y, x))
                while True:
                    if len(d) == 0:
                        answer += 1
                        break
                    curr_y, curr_x = d.popleft()
                    if visited[curr_y][curr_x] == False:
                        visited[curr_y][curr_x] = True
                        for i in range(4):
                            new_y = curr_y + dys[i]
                            new_x = curr_x + dxs[i]
                            if worldmap_boundary(new_y, new_x):
                                if visited[new_y][new_x] == False:
                                    d.append((new_y, new_x))
    
    print(answer)