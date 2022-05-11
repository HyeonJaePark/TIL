import sys

def solution(s):
    s += ' '
    ans_max = -sys.maxsize
    ans_min = sys.maxsize
    
    tmp = ''
    for i in s:
        if i == ' ':
            if len(tmp):
                tmp = int(tmp)
                if tmp > ans_max:
                    ans_max = tmp
                if tmp < ans_min:
                    ans_min = tmp
            tmp = ''
        else:
            tmp += i
    return str(ans_min) + ' ' + str(ans_max)

s = "-1 -2 -3 -4"
print(solution(s))