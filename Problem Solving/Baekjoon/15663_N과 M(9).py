from itertools import permutations

n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))
answer = set()


for x in permutations(s, m):
    answer.add(x)
for a in sorted(answer):
    print(str(a)[1:-1].replace(',', ''))
