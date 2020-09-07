N=7
L=[218, 786, 704, 233, 645, 728, 389]

#N = int(input())
#L = list(map(int, input().split()))

L.sort()

from bisect import*
ans = 0
for i in range(N):
    for j in range(i+1, N):
        a = L[i]
        b = L[j]
        r = bisect_left(L, (a + b))
        l = j + 1
        ans += max(0, r-l)
print(ans)
