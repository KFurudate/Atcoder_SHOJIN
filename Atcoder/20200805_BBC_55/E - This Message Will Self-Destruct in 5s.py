ffrom collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
dic = defaultdict(int)

ans = 0
#j-i = Ai+A　⇄　j-A[j] = A[i]+i
for i in range(n):
    Sum = A[i] + i
    dic[Sum] += 1
    Dif = i - A[i]
    ans += dic[Dif]
print(ans)

