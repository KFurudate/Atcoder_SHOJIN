n = int(input())
h = list(map(int, input().split()))
h.reverse()

ans = 0
val = 0

for i in range(1, n):
    if h[i-1] <= h[i]:
        val +=1
    else:
        val = 0
    ans = max(ans, val)
print(ans)