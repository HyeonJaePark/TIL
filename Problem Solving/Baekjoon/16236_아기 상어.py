import sys
from collections import deque
input = sys.stdin.readline

dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

def boundary(x, y):
    return True if ((0 <= x < n) and (0 <= y < n)) else False


def can_eat(x, y):
    return True if (0 < worldmap[x][y] < shark_size) else False


def can_move(x, y):
    return True if worldmap[x][y] <= shark_size else False


n = int(input())
worldmap = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        if worldmap[i][j] == 9:
            worldmap[i][j] = 0
            shark_pos = (i, j)
            visited[i][j] = True

shark_size = 2
cnt_eat_fish = 0
sec = 0
tf_find = False
tf_time = 0
tf_crod = []

d = deque()
d.append((shark_pos[0], shark_pos[1], 0))

while True:
    if len(d) == 0 and tf_find == False:
        print(sec)
        break
    if tf_find == True and len(d) == 0:
        tf_crod.sort(key=lambda x:(x[0], x[1]))
        x, y = tf_crod[0]
        sec += tf_time
        d = deque()
        d.append((x, y, 0))
        visited = [
            [False for _ in range(n)]
            for _ in range(n)
        ]
        visited[x][y] = True
        worldmap[x][y] = 0
        tf_crod = []
        tf_find = False
        tf_time = 0
        cnt_eat_fish += 1
        if cnt_eat_fish == shark_size:
            shark_size += 1
            cnt_eat_fish = 0
            
    x, y, dis = d.popleft()
    if tf_find == True and tf_time <= dis:
        continue
    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        if boundary(nx, ny) == True:
            if can_eat(nx, ny) == True:
                visited[nx][ny] = True
                tf_crod.append((nx, ny))
                if tf_find == False:
                    tf_time = dis + 1
                tf_find = True
            else:
                if tf_find == False and can_move(nx, ny) == True and visited[nx][ny] == False:
                    d.append((nx, ny, dis + 1))
                    visited[nx][ny] = True