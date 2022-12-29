import sys
from queue import PriorityQueue
input = sys.stdin.readline

pq = PriorityQueue()

n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if pq.empty():
            print(0)
        else:
            print(pq.get()[1])
    else:
        pq.put((abs(x), x))
