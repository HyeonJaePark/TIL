import sys
input = sys.stdin.readline

n = int(input())
costs = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [None for _ in range(1 << n)]
    for _ in range(n)
]
INF = sys.maxsize


def find_path(last, visited):
    if visited == (1 << n) - 1:
        return costs[last][0] or INF

    if dp[last][visited] is not None:
        return dp[last][visited]

    tmp = INF
    for i in range(n):
        if visited & (1 << i) == 0 and costs[last][i] != 0:
            tmp = min(tmp, find_path(i, visited | (1 << i)) + costs[last][i])
    dp[last][visited] = tmp
    return tmp


print(find_path(0, 1))
