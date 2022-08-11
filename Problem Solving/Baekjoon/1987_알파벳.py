import sys
input = sys.stdin.readline


def inbound(x, y):
    global r, c
    return True if (0 <= x < r) and (0 <= y < c) else False


def dfs(x, y, visited, cnt):
    global answer
    visited[board[x][y]] = True
    cnt += 1
    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if inbound(nx, ny) and not visited[board[nx][ny]]:
            dfs(nx, ny, visited, cnt)
    visited[board[x][y]] = False
    answer = max(answer, cnt)
    if answer == 26:
        print(answer)
        exit(0)
    return


r, c = map(int, input().split())
board = [
    list(map(lambda x: ord(x) - 65, input().rstrip()))
    for _ in range(r)
]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
answer = 1

dfs(0, 0, [False for _ in range(26)], 0)
print(answer)


# import sys
# input = sys.stdin.readline

# def alp(y, x):
#     global res

#     tmp = set([(y, x, db[0][0])])

#     while tmp:
#         y, x, chk = tmp.pop()

#         for i, j in dyx:
#             dy, dx = y + i, x + j
#             if 0 <= dy < r and 0 <= dx < c:
#                 if not db[dy][dx] in chk:
#                     tmp.add((dy, dx, chk + db[dy][dx]))
#                     res = max(res, len(chk) + 1)
#                     if res >= 26:
#                         return

# r, c = map(int, input().strip().split())
# db = [list(input().strip()) for _ in range(r)]
# res = 1
# dyx = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# alp(0, 0)

# print(res)
