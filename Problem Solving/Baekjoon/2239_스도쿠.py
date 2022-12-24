import sys


def print_board():
    for i in range(9):
        for j in range(9):
            print(board[i][j], end='')
        print()


def dfs(dep):
    if dep == len(blanks):
        print_board()
        sys.exit(0)

    r, c = blanks[dep]
    visit = [False for _ in range(10)]

    for i in range(9):
        if board[r][i] != 0:
            visit[board[r][i]] = True

    for i in range(9):
        if board[i][c] != 0:
            visit[board[i][c]] = True

    startX = (r // 3) * 3
    startY = (c // 3) * 3
    for i in range(startX, startX + 3):
        for j in range(startY, startY + 3):
            if board[i][j] != 0:
                visit[board[i][j]] = True

    for i in range(1, 10):
        if not visit[i]:
            board[r][c] = i
            dfs(dep + 1)
            board[r][c] = 0


board = [
    list(map(int, input()))
    for _ in range(9)
]
blanks = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blanks.append((i, j))

dfs(0)
