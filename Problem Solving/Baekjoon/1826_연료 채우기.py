import sys
import heapq
input = sys.stdin.readline

n = int(input())
stations = [
    list(map(int, input().split()))
    for _ in range(n)
]
l, p = map(int, input().split())
stations.sort(key=lambda x:(x[0], x[1]))

idx, answer = 0, 0
q = []

while p < l:
    while idx < n and p >= stations[idx][0]:
        heapq.heappush(q, (-stations[idx][1], stations[idx][1]))
        idx += 1
    if len(q) == 0:
        print(-1)
        exit(0)
    p += heapq.heappop(q)[1]
    answer += 1

print(answer)