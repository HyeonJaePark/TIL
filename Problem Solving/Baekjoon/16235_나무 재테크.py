import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m, k = map(int, input().split())

    a = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    trees = [
        list(map(int, input().split()))
        for _ in range(m)
    ]

    print(a, trees)