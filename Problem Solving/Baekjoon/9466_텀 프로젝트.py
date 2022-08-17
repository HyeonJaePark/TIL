import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(student):
    team = [student]
    candidate = set()
    candidate.add(student)
    stack = [student]
    visited[student] = True

    while stack:
        nstudent = preferences[stack.pop()]

        if nstudent in candidate:
            tmp = list(dict.fromkeys(team))
            return tmp[tmp.index(nstudent):]
        elif not visited[nstudent]:
            team.append(nstudent)
            stack.append(nstudent)
            candidate.add(nstudent)
            visited[nstudent] = True

    return []


t = int(input())
for _ in range(t):
    n = int(input())
    preferences = [0]
    preferences[1:] = list(map(int, input().split()))
    visited = [False for _ in range(n + 1)]
    answer = []
    for i in range(1, n + 1):
        if not visited[i]:
            answer += dfs(i)
    print(n - len(answer))
