import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def postorder(s, e):
    if s >= e:
        return
    if s == e - 1:
        print(t[s])
        return
    i = s + 1
    while i < e:
        if t[s] < t[i]:
            break
        i += 1
    postorder(s+1, i)
    postorder(i, e)
    print(t[s])


t = []
idx = 0
while True:
    try:
        t.append(int(input()))
        idx += 1
    except:
        break

postorder(0, idx)