h1, m1, h2, m2, k = map(int, input().split())

hour = h2-h1
min = 60*hour + (m2-m1)
ans = min-k
print(ans)
