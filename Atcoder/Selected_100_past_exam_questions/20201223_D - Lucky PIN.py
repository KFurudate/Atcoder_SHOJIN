#TLE
n = int(input())
S = input()

ans = []
cnt = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if S[i]+S[j]+S[k] not in ans:
                cnt += 1
                ans.append(S[i]+S[j]+S[k])

print(cnt)

##################################
n = int(input())
S = input()

cnt = 0
for i in range(1000):
    idx = 0
    if i < 10:
        s_i = "00" + str(i)
    elif i < 100:
        s_i = "0" + str(i)
    else:
        s_i = str(i)

    for s in S:
        if s_i[idx] == s:
            idx += 1
            if idx == 3:
                cnt += 1
            if idx >= len(s_i):
                break

print(cnt)
##################################

n = int(input())
S = input()

cnt = 0
for i in range(10):
    idx_i = S.find(str(i))
    if idx_i != -1:
        for j in range(10):
            idx_j = S.find(str(j), idx_i+1)
            if idx_j != -1:
                for k in range(10):
                    idx_k = S.find(str(k), idx_j+1)
                    if idx_k != -1:
                        cnt += 1
print(cnt)






