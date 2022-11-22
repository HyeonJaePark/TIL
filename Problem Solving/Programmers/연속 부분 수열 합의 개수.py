# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    answer = set()

    for i in range(len(elements)):
        tmp = 0
        for j in range(len(elements)):
            tmp += elements[(i + j) % len(elements)]
            answer.add(tmp)

    return len(answer)


elements = [7, 8, 1, 1, 4]
print(solution(elements))
