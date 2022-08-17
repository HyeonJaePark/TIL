import sys
input = sys.stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node] = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        return tree[node]


def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff

    if start != end:
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)


def subsequence_sum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[node]
    
    return subsequence_sum(node*2, start, (start+end)//2, left, right) + subsequence_sum(node*2+1, (start+end)//2+1, end, left, right)

n, m, k = map(int, input().split())

arr = [int(input()) for _ in range(n)]
tree = [0 for _ in range(1000000 * 4)]

init(1, 0, n - 1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b-1]
        arr[b-1] = c
        update(1, 0, n-1, b - 1, diff)
    else:
        print(subsequence_sum(1, 0, n-1, b-1, c-1))