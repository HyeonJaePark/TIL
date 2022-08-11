# solution 1

from itertools import combinations

n, m = map(int, input().split())

for com in list(combinations([x for x in range(1, n + 1)], m)):
    for i in com:
        print(i, end=' ')
    print()

# solution 2

def solve(x, y, a):
    if x == m:
        print(a[1:])
        return
    for i in range(y + 1, n + 1):
        if not visited[i]:
            visited[i] = True
            solve(x + 1, i, a+' '+str(i))
            visited[i] = False

n, m = map(int, input().split())
visited = [False for _ in range(n + 1)]
solve(0, 0, '')