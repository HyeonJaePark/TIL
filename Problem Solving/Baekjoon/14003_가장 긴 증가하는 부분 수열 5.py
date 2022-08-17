import sys
input = sys.stdin.readline


def binarysearch(left, right, target):
    while left < right:
        mid = (left + right) // 2

        if answer[mid] < target:
            left = mid + 1
        elif answer[mid] > target:
            right = mid
        else:
            right = mid
            return (right, True)

    return (right, False)


n = int(input())
a = list(map(int, input().split()))
answer = [0 for _ in range(n)]
answer[0] = a[0]

j = 0
for i in range(1, n):
    print(j, i)
    if answer[j] < a[i]:
        answer[j + 1] = a[i]
        j += 1
    elif answer[j] > a[i]:
        idx, tf = binarysearch(0, j, a[i])
        if not tf:
            answer = answer[:idx] + [a[i]] + answer[idx:]
            j += 1


print(j + 1)
print(str(answer[:j+1])[1:-1].replace(',', ''))
