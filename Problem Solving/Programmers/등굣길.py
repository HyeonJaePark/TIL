def solution(m, n, puddles):
    board = [
        [0 for _ in range(101)]
        for _ in range(101)
    ]
    for r, c in puddles:
        board[r][c] = False

    board[1][0] = 1
    for i in range(1, n + 1):
        for j in range(i, m + 1):
            if board[i][j] is not False:
                board[i][j] = int(board[i][j - 1]) + int(board[i - 1][j])
        for j in range(i, n + 1):
            if board[j][i] is not False:
                board[j][i] = int(board[j - 1][i]) + int(board[j][i - 1])

    for i in range(n + 1):
        for j in range(m + 1):
            print(board[i][j], end=' ')
        print()

    return board[n][m] % 1000000007


m = 2
n = 5
puddles = [[3, 2]]
print(solution(m, n, puddles))
