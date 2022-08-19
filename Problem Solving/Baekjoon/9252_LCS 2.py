# 알고리즘 참고자료
# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence

a = input()
b = input()
answer = ''
dxs = [-1, 0]
dys = [0, -1]

if len(a) > len(b):
    a, b = b, a

lcs = [
    [0 for _ in range(len(b) + 1)]
    for _ in range(len(a) + 1)
]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

r, c = len(a), len(b)
p = lcs[r][c]
for i in lcs:
    print(i)
if lcs[r][c] == 0:
    print(0)
else:
    print(p)
    while len(answer) < p:
        tf = False
        for i in range(2):
            nr, nc = r + dxs[i], c + dys[i]
            if lcs[r][c] == lcs[nr][nc]:
                r, c = nr, nc
                tf = True
                break
        if not tf:
            r, c = r - 1, c - 1
            answer += a[r]
    print(answer[::-1])
