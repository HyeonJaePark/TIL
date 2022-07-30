from itertools import combinations
e = input()

answer = []
stack = []
brakect = []

for i, x in enumerate(e):
    if x == '(':
        stack.append(i)
    elif x == ')':
        brakect.append([stack.pop(), i])

for i in range(1, len(brakect) + 1):
    for c in combinations(brakect, i):
        tmp = [x for s in c for x in s]
        ne = [x for _, x in enumerate(e) if _ not in tmp]
        answer.append(''.join(ne))

for i in sorted(set(answer)):
    print(i)
