n = int(input())
a = list(map(int, input().split()))

ans = 1
x = 0

for i in range(n-1):
    if a[i] < a[i+1]:
        if x == -1:
            ans += 1
            x = 0
        elif x == 0:
            x = 1
    elif a[i] > a[i+1]:
        if x == 1:
            ans += 1
            x = 0
        elif x == 0:
            x = -1
print(ans)