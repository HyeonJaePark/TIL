import sys

input = sys.stdin.readline

N = int(input())
numbers = [int(x) for x in input().split()]
M = int(input())

dp = [
    [0 for _ in range(N + 1)]
    for _ in range(N + 1)
]

for i in range(N):
    dp[i][i] = 1

for i in range(N - 1):
    if numbers[i] == numbers[i + 1]:
        dp[i][i + 1] = 1

for i in range(2, N):
    for j in range(N - i):
        if numbers[j] == numbers[j + i] and \
            dp[j + 1][j + i - 1] == 1:
            dp[j][j + i] = 1


for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S - 1][E - 1])