n = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(2, 1001):
    cnt = 0
    for a in A:
        if a%i==0:
            cnt += 1
    ans.append((cnt, i))

ans = sorted(ans, reverse=True)
print(ans[0][1])
