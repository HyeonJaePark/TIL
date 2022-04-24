from collections import deque

def solution(s):
    answer = len(s)
    close = [')', ']', '}']
    open = ['(', '[', '{']
    for i in range(len(s)):
        d = deque()
        for j in range(i, len(s) + i):
            curr_bracket = s[j % len(s)]
            if curr_bracket in open:
                d.append(curr_bracket)
            else:
                try:
                    latest_bracket = d.pop()
                    if close.index(curr_bracket) != open.index(latest_bracket):
                        answer -= 1
                        break
                except IndexError:
                    answer -= 1
                    break
    return answer if len(s) % 2 == 0 else 0

s = "{"
print(solution(s))