n = int(input())
S = input()

ans = 0
for i in range(1, n):
    X = S[:i]
    Y = S[i:]
    print(X)
    print(Y,"*")
    cnt = 0
    for x in set(X):
        if x in Y:
            cnt += 1
    ans = max(cnt, ans)
print(ans)