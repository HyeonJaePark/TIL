from collections import deque


def solution(maps):
    def inbound(r, c):
        return True if (0 <= r < len(maps)) and (0 <= c < len(maps[0])) and maps[r][c] == 1 else False

    visited = [
        [False for _ in range(len(maps[0]))]
        for _ in range(len(maps))
    ]
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    d = deque([(0, 0, 1)])
    visited[0][0] = 1

    while d:
        cr, cc, cd = d.popleft()

        for i in range(4):
            nr = cr + dxs[i]
            nc = cc + dys[i]
            nd = cd + 1
            if inbound(nr, nc):
                if visited[nr][nc] is False:
                    visited[nr][nc] = nd
                    d.append((nr, nc, nd))

    return visited[-1][-1] if visited[-1][-1] is not False else -1


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
print(solution(maps))
