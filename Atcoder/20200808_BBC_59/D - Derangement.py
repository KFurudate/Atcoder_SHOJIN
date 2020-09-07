n = int(input())
P = list(map(int, input().split()))

ans = 0
Cnt = []
for idx, p in enumerate(P, 1):
    if idx == p:
        Cnt.append(idx)
#print(Cnt)
if len(Cnt) == 0:
    ans = 0

elif len(Cnt) == 2:
    ans += Cnt[1] - Cnt[0]

elif len(Cnt) %2:
    for i in range(1, len(Cnt), 2):
        if i == 0:
            ans += Cnt[i+1] - Cnt[i]
        elif i == len(Cnt)-1:
            ans += Cnt[i] - Cnt[i-1]
        else:
            ans += min(Cnt[i] - Cnt[i-1], Cnt[i+1] - Cnt[i])
else:
    for i in range(0, len(Cnt), 2):
        if i == 0:
            ans += Cnt[i+1] - Cnt[i]
        elif i == len(Cnt)-1:
            ans += Cnt[i] - Cnt[i-1]
        else:
            ans += min(Cnt[i] - Cnt[i-1], Cnt[i+1] - Cnt[i])

print(ans)

########################

n = int(input())
P = list(map(int, input().split()))

Cnt = []
cnt = 0
ans = 0
for idx, p in enumerate(P, 1):
    if idx == p:
        Cnt.append(idx)
        cnt += 1
    else:
        cnt = 0
    if cnt == 2:
        ans -= 1
        cnt = 0

ans += len(Cnt)
print(ans)







