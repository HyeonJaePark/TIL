import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    command = list(input())
    n = int(input())
    dir = 1 # 홀수 dir = 순방향, 짝수 dir = 역방향
    error = False
    if n == 0:
        input()
        if 'D' in command:
            error = True
        else:
            arr = []
    else:
        arr = deque(map(int, input().rstrip(']\n').lstrip('[').split(',')))
        for c in command:
            if c == 'R':
                dir += 1
            elif c == 'D':
                if len(arr) > 0:
                    if dir % 2 == 0:
                        arr.pop()
                    else:
                        arr.popleft()
                else:
                    error = True
                    break
    if error == True:
        print('error')
    else:
        if dir % 2 == 0:
            print(str(list(arr)[::-1]).replace(' ', ''))
        else:
            print(str(list(arr)).replace(' ', ''))