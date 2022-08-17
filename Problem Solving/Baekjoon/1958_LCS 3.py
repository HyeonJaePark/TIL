a = input()
b = input()
c = input()

lcs = [
    [
        [0 for _ in range(len(a) + 1)]
        for _ in range(len(b) + 1)
    ]
    for _ in range(len(c) + 1)
]

for i in range(1, len(c) + 1):
    for j in range(1, len(b) + 1):
        for k in range(1, len(a) + 1):
            if c[i - 1] == b[j - 1] and b[j - 1] == a[k - 1]:
                lcs[i][j][k] = lcs[i - 1][j - 1][k - 1] + 1
            else:
                lcs[i][j][k] = max(
                    lcs[i][j][k - 1], max(lcs[i - 1][j][k], lcs[i][j - 1][k]))

print(lcs[-1][-1][-1])
