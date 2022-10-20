from collections import defaultdict, deque
import sys


def solution(n, wires):
    answer = sys.maxsize

    wires_dict = defaultdict(list)
    for wire in wires:
        x, y = wire
        wires_dict[x].append(y)
        wires_dict[y].append(x)

    for wire in wires:
        cx, cy = wire

        visited = [False for _ in range(n + 1)]
        d = deque([1])
        cnt = 0

        while d:
            node = d.popleft()
            visited[node] = True
            cnt += 1

            for nd in wires_dict[node]:
                if (node == cx and nd == cy) or \
                        (node == cy and nd == cx):
                    continue
                if not visited[nd]:
                    d.append(nd)

        answer = min(answer, abs(n - (2 * cnt)))

    return answer


n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]

print(solution(n, wires))
