import math

n = int(input())

for _ in range(n):
    m = int(input())
    answer = 0
    for i in range(m, 0, -1):
        answer += math.log10(i)
    print(math.floor(answer) + 1)