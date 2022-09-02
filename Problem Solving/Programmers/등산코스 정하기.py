import heapq
import sys
from collections import defaultdict


def solution(n, paths, gates, summits):
    answer_summit = n
    answer_intensity = sys.maxsize
    summit_set = set(summits)
    visited = [sys.maxsize for _ in range(n+1)]

    costs = defaultdict(dict)
    for path in paths:
        start, dest, cost = path
        costs[start][dest] = cost
        costs[dest][start] = cost

    pq = []
    for gate in gates:
        visited[gate] = 0
        for next_node in costs[gate]:
            heapq.heappush(pq, (costs[gate][next_node], next_node))

    while pq:
        cost, node = heapq.heappop(pq)
        if cost >= visited[node]:
            continue
        visited[node] = cost
        if node in summit_set:
            continue
        for next_node in costs[node]:
            if visited[next_node] <= cost:
                continue
            heapq.heappush(pq, (max(cost, costs[node][next_node]), next_node))

    for summit in summits:
        if answer_intensity > visited[summit]:
            answer_intensity = visited[summit]
            answer_summit = summit
        elif answer_intensity == visited[summit]:
            if answer_summit > summit:
                answer_summit = summit

    return [answer_summit, answer_intensity]


N = 7
PATHS = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [
    2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
GATES = [3, 7]
SUMMITS = [1, 5]

print(solution(n=N, paths=PATHS, gates=GATES, summits=SUMMITS))
