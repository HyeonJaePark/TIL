import sys
input = sys.stdin.readline

s = set()
n = int(input())
for _ in range(n):
    c = input().split()
    if len(c) > 1:
        c, x = c[0], int(c[1])
    else:
        c = c[0]
    if c == 'add':
        s.add(x)
    elif c == 'remove':
        s.discard(x)
    elif c == 'toggle':
        try:
            s.remove(x)
        except:
            s.add(x)
    elif c == 'check':
        if x in s:
            print(1)
        else:
            print(0)
    elif c == 'all':
        s = set({x for x in range(1, 21)})
    elif c == 'empty':
        s = set()
