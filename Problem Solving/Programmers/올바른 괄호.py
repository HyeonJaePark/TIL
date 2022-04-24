def solution(s):
    tmp = 0
    for bracket in s:
        if bracket == '(':
            tmp += 1
        else:
            if tmp <= 0:
                return False
            else:
                tmp -=1
        
    return True if tmp == 0 else False

s = '(()('
print(solution(s))