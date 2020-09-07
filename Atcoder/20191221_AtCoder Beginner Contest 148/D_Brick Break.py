n = int(input())
a_n = list(map(int, input().split()))
nxt = 1
ans = 0

for a in a_n:
    if nxt == a:
        nxt += 1
    else:
        ans += 1

if ans == n:
    ans = -1

print(ans)




