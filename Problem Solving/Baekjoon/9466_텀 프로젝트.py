import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    preferences = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(n + 1)]
    s, answer = [], 0

    for preference in preferences:
        visited[preference] += 1

    for i in range(1, n + 1):
        if not visited[i]:
            s.append(i)
            visited[i] -= 1

    while s:
        c = s.pop()
        answer += 1

        visited[preferences[c]] -= 1
        if not visited[preferences[c]]:
            s.append(preferences[c])

    print(answer)


# sys.setrecursionlimit(10**6)


# def dfs(student):
#     team = [student]
#     stack = [student]
#     visited[student] = True

#     while stack:
#         cstudent = stack.pop()
#         nstudent = preferences[cstudent]

#         if nstudent in team:
#             tmp = list(dict.fromkeys(team))
#             tmp = tmp[tmp.index(nstudent):]
#             return tmp
#         elif not visited[nstudent]:
#             team.append(nstudent)
#             visited[nstudent] = True
#             stack.append(nstudent)

#     return []


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     preferences = [0]
#     preferences[1:] = list(map(int, input().split()))
#     visited = [False for _ in range(n + 1)]
#     answer = []
#     for i in range(1, n + 1):
#         if not visited[i]:
#             answer += dfs(i)
#     print(n - len(answer))
