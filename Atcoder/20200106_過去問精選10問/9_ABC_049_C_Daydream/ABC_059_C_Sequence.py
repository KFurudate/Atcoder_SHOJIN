n = int(input())
a = list(map(int, input().split()))
A = []
cnt = 0

for i in range(n-1):
    A.append(a[i])
    if sum(A) > 0:
        while sum(A) + a[i+1] >= 0:
            a[i+1] -= 1
            cnt += 1

    elif sum(A) < 0:
        while sum(A) + a[i+1] <= 0:
            a[i+1] += 1
            cnt += 1

if sum(a) == 0:
    cnt += 1

print(cnt)