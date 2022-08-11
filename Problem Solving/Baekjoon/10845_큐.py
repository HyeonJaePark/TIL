from collections import deque
import sys
input = sys.stdin.readline


n = int(input())

q = deque()

for _ in range(n):
    order = input().split()

    if order[0] == 'push':
        q.append(order[1])
    elif order[0] == 'pop':
        try:
            print(q.popleft())
        except:
            print(-1)
    elif order[0] == 'size':
        print(len(q))
    elif order[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)
