n = int(input())
stairs = [0 for _ in range(n + 1)]
for i in range(n):
    stairs[i] = int(input())
dp = [
    [0 for _ in range(3)]
    for _ in range(n + 1)
]

dp[1][1] = stairs[0]

for i in range(2, n + 1):
    dp[i][2] = dp[i - 1][1] + stairs[i - 1]
    dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + stairs[i - 1]

print(max(dp[n][1], dp[n][2]))