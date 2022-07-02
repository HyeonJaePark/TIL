import sys

def solution(x):
    for crash in crashes:
        if crash in str(x):
            return sys.maxsize
    
    return (abs(n - x) + len(str(x)))

n = int(input())
m = int(input())
crashes = []
if m > 0:
    crashes = list(map(str, input().split()))

curr_channel = 100
answer = abs(curr_channel - n)

if answer != 0:
    for i in range(1000000):
        answer = min(solution(i), answer)
print(answer)