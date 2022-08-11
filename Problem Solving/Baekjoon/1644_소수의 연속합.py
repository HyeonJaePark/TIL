n = int(input())
primes = []

ip = [False, False] + [True] * (n - 1)
for i in range(2, n + 1):
    if ip[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            ip[j] = False

print(primes)
answer = 0
left, right = 0, 0
try:
    tmp_sum = primes[0]
except:
    print(0)
else:
    while left <= len(primes) - 1:
        if tmp_sum < n:
            if right < len(primes) - 1:
                right += 1
            tmp_sum += primes[right]
        elif tmp_sum > n:
            tmp_sum -= primes[left]
            left += 1
        else:
            print(tmp_sum, n, left, right, answer)
            answer += 1
            tmp_sum -= primes[left]
            left += 1
    print(answer)
