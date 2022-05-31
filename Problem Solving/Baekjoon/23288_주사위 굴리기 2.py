import sys
from collections import deque

input = sys.stdin.readline

# 동쪽 0, 남쪽 1, 서쪽 2, 북쪽 3
# top, up, right, left, down, bottom
dice = [x for x in range(1, 7)]

def move_check(x, y, dir):
    global n, m
    if dir == 0:
        if y == m - 1:
            return (x, y - 1, 2)
        return (x, y + 1, dir)
    elif dir == 1:
        if x == n - 1:
            return (x - 1, y, 3)
        return (x + 1, y, dir)
    elif dir == 2:
        if y == 0:
            return (x, y + 1, 0)
        return (x, y - 1, dir)
    elif dir == 3:
        if x == 0:
            return (x + 1, y, 1)
        return (x - 1, y, dir)


def dice_planar(dir):
    global dice

    if dir == 0:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]    
    elif dir == 1:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    elif dir == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif dir == 3:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]


def next_dir(x, y, dir):
    global worldmap

    world_number = worldmap[x][y]
    dice_bottom = dice[5]

    if world_number < dice_bottom:
        dir = (dir + 1) % 4
    elif world_number > dice_bottom:
        dir = (dir - 1) % 4
    
    return dir


def map_check(x, y):
    global n, m
    return True if ((x >= 0) and (x < n) and (y >= 0) and (y < m)) else False


def get_score(x, y):
    global worldmap

    world_number = worldmap[x][y]
    tmpmap = [
        [False for _ in range(m)]
        for _ in range(n)
    ]
    tmpmap[x][y] = True

    d = deque()
    d.append((x, y))
    print(d)
    tile = 0
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    while True:
        if len(d) == 0:
            return tile * world_number
        curr_x, curr_y = d.popleft()
        for i in range(4):
            if map_check(curr_x + dxs[i], curr_y + dys[i]):
                if world_number == worldmap[curr_x + dxs[i]][curr_y + dys[i]] and tmpmap[curr_x + dxs[i]][curr_y + dys[i]] == False:
                    d.append((curr_x + dxs[i], curr_y + dys[i]))
                    tmpmap[curr_x + dxs[i]][curr_y + dys[i]] = True
        tile += 1
    

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    
    worldmap = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    score = 0
    dir = 0
    x, y = 0, 0

    for _ in range(k):
        print(dir)
        x, y, dir = move_check(x, y, dir)
        dice_planar(dir)
        score += get_score(x, y)
        dir = next_dir(x, y, dir)
        print(score)
        print('-----------')

    print(score)