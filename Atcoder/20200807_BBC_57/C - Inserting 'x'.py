from collections import Counter

S = input()
C = Counter(S)
print(C)

Keys = tuple(C.keys())

cnt = 0
for k in Keys:
    if k != "x" and C[k]%2:
        cnt += 1

if not cnt % 2:
    print(-1)

############################
S = input()

l = 0
r = len(S)-1
cnt = 0

while l < r:
    if S[l] == S[r]:
        l += 1
        r += 1
    elif S[l] == "x":
        l += 1
        cnt += 1
    elif S[r] == "x":
        r += 1
        cnt += 1
    else:
        print(-1)
        exit()

print(cnt)