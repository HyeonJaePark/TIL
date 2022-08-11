n, m = map(int, input().split())


def dfs(depth, arr, curr):
    if depth == m:
        print(str(arr)[1:-1].replace(',', ''))
        return
    for i in range(curr, n + 1):
        if len(arr) and arr[-1] <= i:
            arr.append(i)
            dfs(depth + 1, arr, curr)
            arr.pop()


for i in range(1, n + 1):
    dfs(1, [i], i)
