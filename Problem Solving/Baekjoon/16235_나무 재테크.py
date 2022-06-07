import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
worldmap = [
    [5 for _ in range(n)]
    for _ in range(n)
]
a = [
    list(map(int, input().split()))
    for _ in range(n)
]
trees = [
    [deque() for _ in range(n)]
    for _ in range(n)
]
dxs = [-1, -1, -1, 0, 0, 1, 1, 1]
dys = [-1, 0, 1, -1, 1, -1, 0, 1]
for _ in range(m):
    r, c, age = map(int, input().split())
    trees[r - 1][c - 1].append(age)
    
for _ in range(k):
    # Spring and Summer
    for r in range(n):
        for c in range(n):
            new_trees = deque()
            new_land = 0
            for tree in trees[r][c]:
                if worldmap[r][c] >= tree:
                    worldmap[r][c] -= tree
                    new_trees.append(tree + 1)
                else:
                    new_land += (tree // 2)
            worldmap[r][c] += new_land
            trees[r][c] = new_trees
    # Fall and Winter
    tmp_trees = []
    for r in range(n):
        for c in range(n):
            for tree in trees[r][c]:
                if tree % 5 == 0:
                    for i in range(8):
                        if (r + dxs[i] >= 0 and r + dxs[i] < n and c + dys[i] >= 0 and c + dys[i] < n):
                            tmp_trees.append((r + dxs[i], c + dys[i]))
            worldmap[r][c] += a[r][c]
    for tmp_tree in tmp_trees:
        r, c = tmp_tree
        trees[r][c].appendleft(1)
        
answer = 0
for r in range(n):
    for c in range(n):
        answer += len(trees[r][c])
print(answer)