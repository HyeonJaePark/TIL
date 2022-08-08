t = int(input())
for _ in range(t):
    n = int(input())
    dp = [1 for _ in range(12)]
    dp[1:3] = 1, 2
    for i in range(3, n + 1):
        dp[i] = sum(dp[i - 3:i])
    print(dp[n])