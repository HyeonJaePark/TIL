import sys
from collections import deque
input = sys.stdin.readline

def bound(x, y):
    return True if ((0 <= x < n) and (0 <= y < n)) else False

n = int(input())
picture = [
    list(input().rstrip())
    for _ in range(n)
]
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# normal
normal = 0
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            color = picture[i][j]
            d = deque()
            d.append((i, j))
            visited[i][j] = True
            while d:
                x, y = d.popleft()
                for k in range(4):
                    nx, ny = x + dxs[k], y + dys[k]
                    if bound(nx, ny) == True:
                        if picture[nx][ny] == color and visited[nx][ny] == False:
                            d.append((nx, ny))
                            visited[nx][ny] = True
            normal += 1
            for a in visited:
                print(a)
            print()

# blind
blind = 0
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            color = picture[i][j]
            if color in ['R', 'G']:
                color = ['R', 'G']
            d = deque()
            d.append((i, j))
            visited[i][j] = True
            while d:
                x, y = d.popleft()
                for k in range(4):
                    nx, ny = x + dxs[k], y + dys[k]
                    if bound(nx, ny) == True:
                        if (picture[nx][ny] in color) and (visited[nx][ny] == False):
                            d.append((nx, ny))
                            visited[nx][ny] = True
            blind += 1

print(normal, blind)