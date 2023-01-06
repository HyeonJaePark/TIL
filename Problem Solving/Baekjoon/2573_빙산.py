import sys
from collections import deque
import copy
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0


def inbound(r, c):
    global n, m
    return True if ((0 <= r < n) and (0 <= c < m)) else False


def melting(icebar, board):
    new_icebar = set()
    new_board = copy.deepcopy(board)
    for ice in icebar:
        r, c = ice
        side = 0
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if inbound(nr, nc):
                if board[nr][nc] == 0:
                    side += 1
        new_board[r][c] -= side
        if new_board[r][c] < 0:
            new_board[r][c] = 0
        if new_board[r][c] > 0:
            new_icebar.add((r, c))

    return new_icebar, new_board


def is_splited(icebar):
    if len(icebar) == 0:
        return True

    visited = set()
    d = deque()
    r, c = list(icebar)[0]
    d.append((r, c))
    visited.add((r, c))
    while d:
        r, c = d.popleft()
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if inbound(nr, nc):
                if board[nr][nc] > 0 and (nr, nc) not in visited:
                    d.append((nr, nc))
                    visited.add((nr, nc))

    for node in icebar:
        if node not in visited:
            return True

    return False


n, m = map(int, input().split())
board = [
    list(map(int, input().split()))
    for _ in range(n)
]

ice = set()
for i in range(n):
    for j in range(m):
        if board[i][j] > 0:
            ice.add((i, j))

while True:
    if is_splited(ice.copy()):
        if len(ice) == 0:
            print(0)
        else:
            print(answer)
        break
    ice, board = melting(ice.copy(), board)
    answer += 1
