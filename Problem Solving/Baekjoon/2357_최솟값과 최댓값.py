import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def init(node, start, end):
    if start == end:
        tree[node] = (arr[start], arr[start])
        return tree[node]
    mid = (start+end)//2
    left = init(node*2, start, mid)
    right = init(node*2+1, mid+1, end)
    tree[node] = (min(left[0], right[0]), max(left[1], right[1]))
    return tree[node]


def solve(node, start, end, a, b):
    if end < a or b < start:
        return (1000000000, 0)
    mid = (start+end)//2

    if a <= start and end <= b:
        return tree[node]
    else:
        left = solve(node*2, start, mid, a, b)
        right = solve(node*2+1, mid+1, end, a, b)
        return (min(left[0], right[0]), max(left[1], right[1]))


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0 for _ in range(n*4)]
init(1, 0, n-1)
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b-= 1
    answer = solve(1, 0, n-1, a, b)
    print(answer[0], answer[1])
