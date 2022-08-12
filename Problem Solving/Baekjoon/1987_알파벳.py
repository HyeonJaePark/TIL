import sys
input = sys.stdin.readline


def inbound(x, y):
    global r, c
    return True if (0 <= x < r) and (0 <= y < c) else False


def dfs(x, y):
    answer = 1
    dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    visited = set([(x, y, board[x][y])])

    while visited:
        x, y, letter = visited.pop()
        
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if inbound(nx, ny):
                if not board[nx][ny] in letter:
                    visited.add((nx, ny, letter + board[nx][ny]))
                    answer = max(answer, len(letter) + 1)
                    if answer == 26:
                        break
    
    return answer


r, c = map(int, input().split())
board = [
    list(map(str, input().rstrip()))
    for _ in range(r)
]

print(dfs(0, 0))
