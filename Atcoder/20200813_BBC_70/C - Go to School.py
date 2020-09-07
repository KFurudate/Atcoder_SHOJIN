#TLE
n = int(input())
A = list(map(int, input().split()))

ans = [A.index(i + 1) + 1 for i in range(n)]
print(*ans)

#####################