import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)

answer = sum(x * y for x, y in zip(a, b))
print(answer)
