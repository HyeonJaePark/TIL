import sys
from itertools import combinations
input = sys.stdin.readline

n, c = map(int, input().split())
arr = list(map(int, input().split()))
f = arr[:n//2]
b = arr[n//2:]

front = [0]
back = [0]
for i in range(1, len(f)+1):
    for j in combinations(f, i):
        front.append(sum(j))
for i in range(1, len(b) + 1):
    for j in combinations(b, i):
        back.append(sum(j))
front.sort()
back.sort()

answer = 0

for i in back:
    if i > c:
        continue
    left = 0
    right = len(front)
    while left < right:
        mid = (left + right) // 2
        if front[mid]+i > c:
            right = mid
        else:
            left = mid + 1
    answer += right
print(answer)