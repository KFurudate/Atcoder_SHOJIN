#TLE
S = input()

cnt = 0
idx = 0
while "BW" in S:
    if S[idx:idx + 2] == "BW":
        cnt += 1
        S = S[:idx] + "WB" + S[idx + 2:]
        idx = 0
    else:
        idx += 1

print(cnt)

#################################
#TLE
S = input()

cnt = 0
while "BW" in S:
    cnt += S.count("BW")
    S.replace("BW", "WB")

print(cnt)

#################################
#AC

S = input()

ans = 0
cnt = 0
for i in range(len(S)):
    if S[i] == "B":
        cnt += 1
    else:
        ans += cnt
print(ans)
