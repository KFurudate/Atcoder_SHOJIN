L, R = map(int, input().split())

for i in range(L, L+2020-1):
    for j in range(i+1, i+2020):
        if j > R: break
        ans = min((i*j)%2019, 2019)
        print(ans)