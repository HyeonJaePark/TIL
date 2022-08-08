import sys
from collections import defaultdict, deque
input = sys.stdin.readline

distances = defaultdict(dict)
visited = []
answer_dist = 0
answer_vertex = 0

def solve(vertex, dist):
    global answer_dist, answer_vertex, visited
    if visited[vertex]:
        return
    if answer_dist < dist:
        answer_dist = dist
        answer_vertex = vertex
    visited[vertex] = True
    for nv in distances[vertex]:
        solve(nv, dist + distances[vertex][nv])

if __name__ == '__main__':
    v = int(input())
    visited = [False for _ in range(v + 1)]

    for _ in range(v):
        x, *y, _ = list(map(int, input().split()))
        for i in range(0, len(y), 2):
            try:
                oc = distances[x][y[i]]
            except:
                distances[x][y[i]] = y[i+1]
                distances[y[i]][x] = y[i+1]
            else:
                if oc > y[i+1]:
                    distances[x][y[i]] = y[i+1]
                    distances[y[i]][x] = y[i+1]        
                    
    solve(1, 0)
    visited = [False for _ in range(v + 1)]
    answer_dist = 0
    solve(answer_vertex, answer_dist)
    print(answer_dist)
