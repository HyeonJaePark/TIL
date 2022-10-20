from collections import deque


def solution(order):
    container = deque(x for x in range(1, len(order) + 1))
    sub_container = deque()
    answer = 0

    while True:
        if not len(container):
            if not len(sub_container):
                break
            else:
                if sub_container[-1] == order[answer]:
                    sub_container.pop()
                    answer += 1
                else:
                    break
        else:
            if container[0] == order[answer]:
                container.popleft()
                answer += 1
            else:
                if len(sub_container):
                    if sub_container[-1] == order[answer]:
                        sub_container.pop()
                        answer += 1
                    else:
                        sub_container.append(container.popleft())
                else:
                    sub_container.append(container.popleft())

    return answer


order = [5, 4, 3, 2, 1]
print(solution(order))
