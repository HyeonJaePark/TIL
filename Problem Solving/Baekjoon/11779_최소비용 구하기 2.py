import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
dists = [(0, sys.maxsize) for _ in range(n + 1)]
nodes = defaultdict(dict)
for _ in range(int(input())):
    s, d, c = map(int, input().split())
    try:
        i = nodes[s][d]
    except:
        nodes[s][d] = c
    else:
        if c < i:
            nodes[s][d] = c
start, end = map(int, input().split())


city_cnt = 1
city_path = [end]

d = deque([(start, 0)])
dists[start] = (-1, 0)
while d:
    x, c = d.popleft()
    for nx in nodes[x]:
        nc = nodes[x][nx] + c
        if nc < dists[nx][1]:
            dists[nx] = (x, nc)
            d.append((nx, nc))

tmp = end
while dists[tmp][0] != -1:
    city_path.append(dists[tmp][0])
    tmp = dists[tmp][0]
    city_cnt += 1

print(dists[end][1])
print(city_cnt)
print(str(city_path[::-1])[1:-1].replace(',', ''))