import sys

input = sys.stdin.readline

answer = 0
n = int(input())
arr = [int(x) for x in input().split()]
x = int(input())

visited = set()

for num in arr:
    req_num = x - num
    if req_num in visited:
        answer += 1
    visited.add(num)

print(answer)