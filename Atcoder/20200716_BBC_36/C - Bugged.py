n = int(input())
S = [int(input()) for _ in range(n)]

ans = sum(S)
sort_S = sorted(S)
for s in sort_S:
    if ans % 10 != 0:
        print(ans)
        exit()
    ans -= s

if ans % 10 == 0:
    ans = 0
print(ans)

###################
n = int(input())
S = [int(input()) for i in range(n)]

ans = sum(S)
sort_S = sorted(S)
if ans % 10 != 0:
    print(ans)
    exit()
else:
    for s in sort_S:
        if s % 10 != 0:
            ans -= s
            print(ans)
            exit()
print(0)