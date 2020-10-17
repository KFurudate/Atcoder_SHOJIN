n, m = map(int, input().split())
AB = sorted([list(map(int, input().split())) for _ in range(n)])

cnt, ans = 0, 0
for a, b in AB:
    if cnt + b < m:
        ans += a*b
        cnt += b
    else:
        for i in range(1, b+1):
            ans += a
            cnt += 1
            if cnt == m:
                print(ans)
                exit()