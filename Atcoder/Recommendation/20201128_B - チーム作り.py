n = int(input())

cnt = 0
flg = True
for _ in range(n):
    if cnt == 20:
        cnt = 1
        flg = not flg
    else:
        cnt += 1

if flg:
    ans = cnt
else:
    ans = 21 - cnt

print(ans)