from collections import deque
from collections import defaultdict

n = int(input())
m = int(input())
visited = [False for _ in range(n + 1)]
computers = defaultdict(set)
for _ in range(m):
    x, y = map(int, input().split())
    computers[x].add(y)
    computers[y].add(x)

d = deque()
d.append(1)
visited[1] = True

while True:
    if len(d) == 0:
        print(visited.count(True) - 1)
        break
    c = d.popleft()
    for computer in computers[c]:
        if visited[computer] == False:
            visited[computer] = True
            d.append(computer)
print(visited)