import sys
input = sys.stdin.readline


def solve(c):
    global n

    dp = [
        [0 for _ in range(3)]
        for _ in range(n+1)
    ]

    dp[1] = [board[1][c], board[1][c], board[1][c]]
    if c == 0:
        dp[2] = [sys.maxsize, min(
            dp[1][0], dp[1][2]) + board[2][1], min(dp[1][0], dp[1][1]) + board[2][2]]
    elif c == 1:
        dp[2] = [min(dp[1][1], dp[1][2]) + board[2][0],
                 sys.maxsize, min(dp[1][0], dp[1][1]) + board[2][2]]
    else:
        dp[2] = [min(dp[1][1], dp[1][2]) + board[2][0],
                 min(dp[1][0], dp[1][2]) + board[2][1], sys.maxsize]

    for i in range(3, n+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + board[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + board[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + board[i][2]

    return min(dp[n][(c + 1) % 3], dp[n][(c - 1) % 3])


n = int(input())
board = [[0, 0, 0]] + [
    list(map(int, input().split()))
    for _ in range(n)
]

answer = sys.maxsize

for i in range(3):
    answer = min(answer, solve(i))
print(answer)
