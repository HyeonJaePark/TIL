import sys
from itertools import combinations_with_replacement

def solution(n, info):
    apeach = {key: 0 for key in range(11)}
    
    for score, cnt in enumerate(info):
        apeach[10 - score] = cnt
    
    diff_score = -sys.maxsize
    cases = combinations_with_replacement([x for x in range(11)], n)

    for case in cases:
        ryan = {key : 0 for key in range(11)}
        
        for score in case:
            ryan[score] += 1
        
        ryan_score = 0
        apeach_score = 0

        for score in ryan.keys():
            if (ryan[score] > 0) and (ryan[score] > apeach[score]):
                ryan_score += score
            if (apeach[score] > 0) and (apeach[score] >= ryan[score]):
                apeach_score += score

        if ryan_score - apeach_score > diff_score:
            diff_score = ryan_score - apeach_score
            answer = [x[1] for x in ryan.items()][::-1]

    return answer if diff_score > 0 else [-1]

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))