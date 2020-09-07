import sys
input = lambda: sys.stdin.readline().rstrip()

def choose2(n):
    return n * (n - 1) // 2


n = int(input())
A = list(map(int, input().split()))
A = [a - 1 for a in A]

Cnt = [0] * n
for i in range(n):
    Cnt[A[i]] += 1

tot = 0
for i in range(n):
    tot += choose2(Cnt[i])

for i in range(n):
    ans = tot
    ans -= choose2(Cnt[A[i]])
    ans += choose2(Cnt[A[i]] - 1)
    print(ans)

