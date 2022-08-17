import sys
input = sys.stdin.readline


def binarysearch(left, right, target):
    while left < right:
        mid = (left + right) // 2

        if answer[mid] < target:
            left = mid + 1
        else:
            right = mid

    return right


n = int(input())
a = list(map(int, input().split()))
answer = [0 for _ in range(n)]
answer[0] = a[0]

j = 0
for i in range(1, n):
    if answer[j] < a[i]:
        answer[j + 1] = a[i]
        j += 1
    else:
        idx = binarysearch(0, j, a[i])
        answer[idx] = a[i]

print(j + 1)
