from collections import deque
from collections import defaultdict

# class Node:
#     def __init__(self):
#         self.root = None
#         self.left_child = None
#         self.right_child = None


def dfs(curr_node, visited, sheep, wolf, ans, d, info, track):
    tf = False
    print(visited)
    if info[curr_node] == 0 and curr_node not in track:
        sheep += 1
        ans.append(sheep)
        visited = {curr_node : True}
        track.append(curr_node)
        tf = True
    if info[curr_node] == 1 and curr_node not in track:
        wolf += 1
        track.append(curr_node)
        tf = True

    if sheep == wolf:
        del visited[curr_node]
        if tf:
            track.pop()
        return

    for node in d[curr_node]:
        if node not in visited:
            visited[node] = True
            dfs(node, visited, sheep, wolf, ans, d, info, track)

    del visited[curr_node]
    if tf:
        track.pop()


def solution(info, edges):
    # answer = 0
    # d = {x: Node() for x in range(len(info))}

    # for idx, edge in enumerate(edges):
    #     parent_node, child_node = edge

    #     if d[parent_node].left_child == None:
    #         d[parent_node].left_child = child_node
    #     else:
    #         d[parent_node].right_child = child_node

    #     d[child_node].root = parent_node
    d = defaultdict(list)

    for parent, child in edges:
        d[parent].append(child)
        d[child].append(parent)

    ans = []
    track = []
    visited = {}
    dfs(0, visited, 0, 0, ans, d, info, track)
    ans.sort()
    print(ans)

    return ans[-1]


info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [
    9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
print(solution(info, edges))
