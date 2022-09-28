from collections import defaultdict
import sys
input = sys.stdin.readline

answer = 0

n, k = map(int, input().split())
arr = list(map(int, input().split()))
power = set()

for i, a in enumerate(arr):
    if a not in power:
        if len(power) < n:
            power.add(a)
        elif len(power) == n:
            cnt = defaultdict(int)
            for j in range(n):
                try:
                    if arr[i + j + 1] in power:
                        cnt[arr[i + j + 1]] += 1
                except:
                    pass
            cnt = {k: v for k, v in sorted(
                cnt.items(), key=lambda item: item[1])}
            print(cnt)
            candidate = set()
            if len(cnt) > 0:
                low = cnt[list(cnt.keys())[0]]
                for key in cnt.keys():
                    if cnt[key] == low:
                        candidate.add(key)
                    else:
                        break
