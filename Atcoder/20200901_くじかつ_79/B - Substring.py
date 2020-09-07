S = input()
T = input()
len_T = len(T)

ans = 0
for i in range(len(S) -len_T+ 1):
    cnt = 0
    tmp = S[i : i + len_T]
    for j in range(len_T):
        if tmp[i] == T[i]:
            cnt += 1
    ans = max(ans, cnt)

print(len_T-ans)
