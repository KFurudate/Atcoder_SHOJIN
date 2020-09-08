h1, m1, h2, m2, k = map(int, input().split())

hour = h2 - h1
min = m2 - m1
ans = hour + min - k
print(ans)