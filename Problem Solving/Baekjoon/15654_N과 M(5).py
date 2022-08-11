from itertools import permutations

n, m = map(int, input().split())
s = sorted(list(map(int, input().split())))

for x in permutations(s, m):
    print(str(x)[1:-1].replace(',', ''))
