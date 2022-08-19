import sys
input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split()))

start, end = 0, n - 1
val = solutions[start] + solutions[end]
ans_start, ans_end = 0, n - 1

while start < end:
    mid = solutions[start] + solutions[end]
    if abs(mid) < abs(val):
        val = mid
        ans_start = start
        ans_end = end
        if val == 0:
            break
    if mid < 0:
        start += 1
    else:
        end -= 1
print(solutions[ans_start], solutions[ans_end])
