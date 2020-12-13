n, m, t = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]

a0 = AB[0][0]
ans = n-a0
if ans <= 0:
    print("No")
    exit()

pre_b = a0
for a, b in AB:
    ans -= (a-pre_b)
    if ans <= 0:
        print("No")
        exit()
    ans += (b-a)
    ans = min(ans, n)
    pre_b = b

ans -= (t-b)
if ans <= 0:
    print("No")
else:
    print("Yes")
