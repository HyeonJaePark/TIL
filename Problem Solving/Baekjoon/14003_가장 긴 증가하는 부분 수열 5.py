import sys
input = sys.stdin.readline


def binarysearch(left, right, target):
    while left < right:
        mid = (left + right) // 2

        if track[mid] < target:
            left = mid + 1
        else:
            right = mid

    return right


n = int(input())
a = list(map(int, input().split()))
track = [a[0]]
dp = [(a[0], 1)]

for i in range(1, n):
    if track[-1] < a[i]:
        dp.append((a[i], len(track) + 1))
        track.append(a[i])
    else:
        idx = binarysearch(0, len(track), a[i])
        track[idx] = a[i]
        dp.append((a[i], idx + 1))

max_length = len(track)
answer = []

print(dp)
print(track)

while max_length and dp:
    num, idx = dp.pop()
    if idx == max_length:
        answer.append(num)
        max_length -= 1

print(len(answer))
print(*answer[::-1])
