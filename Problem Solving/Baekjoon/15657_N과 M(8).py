from itertools import permutations

n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))


def dfs(depth, arr):
    if depth == m:
        print(str(arr)[1:-1].replace(',', ''))
        return
    for i in range(n):
        if arr[-1] <= s[i]:
            arr.append(s[i])
            dfs(depth + 1, arr)
            arr.pop()


for i in range(n):
    dfs(1, [s[i]])
