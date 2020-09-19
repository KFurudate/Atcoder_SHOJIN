n = int(input())

cnt = 0
for a in range(n):
    for b in range(n):
        for c in range(1, n):
            if a*b == n-c:
                cnt += 1
print(cnt)


n = int(input())

cnt = 0
for a in range(n):
    for b in range(n):
            if a*b < n:
                cnt += 1
print(cnt)

cnt = 0
for a in range(n):
            if n-1 < n:
                cnt += 1
print(cnt)





