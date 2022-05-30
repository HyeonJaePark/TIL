import sys

input = sys.stdin.readline

# top, up, right, down, left, bottom
dice = [0 for _ in range(6)]

def dice_move(dir):
    global dice
    if dir == 1:
        dice = [dice[4], dice[1], dice[0], dice[3], dice[5], dice[2]]
    elif dir == 2:
        dice = [dice[2], dice[1], dice[5], dice[3], dice[0], dice[4]]
    elif dir == 3:
        dice = [dice[3], dice[0], dice[2], dice[5], dice[4], dice[1]]
    elif dir == 4:
        dice = [dice[1], dice[5], dice[2], dice[0], dice[4], dice[3]]


def move_check(curr_x, curr_y, dir):
    # 동쪽 1 서쪽 2 북쪽 3 남쪽 4
    if dir == 1:
        if curr_y == m - 1:
            return False
        return (curr_x, curr_y + 1)
    elif dir == 2:
        if curr_y == 0:
            return False
        return (curr_x, curr_y - 1)
    elif dir == 3:
        if curr_x == 0:
            return False
        return (curr_x - 1, curr_y)
    elif dir == 4:
        if curr_x == n - 1:
            return False
        return (curr_x + 1, curr_y)


def change_check(curr_x, curr_y):
    global worldmap, dice
    world_number = worldmap[curr_x][curr_y]

    if world_number == 0:
        worldmap[curr_x][curr_y] = dice[5]
    else:
        dice[5] = worldmap[curr_x][curr_y]
        worldmap[curr_x][curr_y] = 0


if __name__ == '__main__':
    n, m, x, y, k = map(int, input().split())

    worldmap = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    moves = list(map(int, input().split()))
    
    for move in moves:
        if move_check(x, y, move):
            curr_pos = move_check(x, y, move)
            x, y = curr_pos
            dice_move(move)
            change_check(x, y)
            print(dice[0])