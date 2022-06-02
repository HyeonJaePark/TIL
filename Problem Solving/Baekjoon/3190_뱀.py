import sys
from collections import deque

input = sys.stdin.readline

snake = deque()
snake.append((0, 0))
dxs = [0, 1, 0, -1] # 동 남 서 북
dys = [1, 0, -1, 0]

def boundary_check(x, y, dir):
    global n
    next_x, next_y = x + dxs[dir], y + dys[dir]

    return True if (next_x >= 0 and next_x < n and next_y >= 0 and next_y < n) else False

def self_crash_check(x, y, dir):
    global snake
    next_x, next_y = x + dxs[dir], y + dys[dir]
    
    if (next_x, next_y) in snake:
        return False
    
    return True


def snake_move(x, y, dir):
    global worldmap, snake
    next_x, next_y = x + dxs[dir], y + dys[dir]
    
    # 1. 뱀의 몸길이를 늘려 머리를 다음칸에 위치
    if (boundary_check(x, y, dir) == False) or (self_crash_check(x, y, dir) == False):
        return (-1, -1)
    snake.append((next_x, next_y))
    
    # 2-1. 사과가 있다면 사과가 없어짐
    if worldmap[next_x][next_y] == 1:
        worldmap[next_x][next_y] = 0
    
    # 2-2. 사과가 없다면 꼬리가 사라짐
    else:
        snake.popleft()

    return next_x, next_y


if __name__ == '__main__':
    dir = 0
    answer = 0
    x, y = 0, 0

    n = int(input())
    k = int(input())
    
    worldmap = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    for _ in range(k):
        r, c = map(int, input().split())
        worldmap[r - 1][c - 1] = 1

    l = int(input())

    turns = [list(input().split()) for _ in range(l)]
    turns.append([sys.maxsize, ''])
    i = 0
    
    while True:
        answer += 1
        x, y = snake_move(x, y, dir)
        if (x, y) == (-1, -1):
            break
        if answer == int(turns[i][0]):
            if turns[i][1] == 'D':
                dir = (dir + 1) % 4
            else:
                dir = (dir - 1) % 4
            i += 1

    print(answer)