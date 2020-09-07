n = int(input())
S = input()

ans = 0
for i in range(1, n-1):
    X = S[:i]
    Y = S[i:]
    tmp = len(set(X) & set(Y))
    ans = max(ans, tmp)
print(ans)



