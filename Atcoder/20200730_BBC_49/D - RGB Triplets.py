n = int(input())
S = input()

A = [0] * n

for i in range(n):
    if S[i] == "R":
        A[i] = 0
    if S[i] == "G":
        A[i] = 1
    if S[i] == "B":
        A[i] = 2
#print(A)

Cnt = [0] * 3
for a in A:
    Cnt[a] += 1

ans = 1
for cnt in Cnt:
    ans *= cnt

# j - i = k -j　
for j in range(n):
    for i in range(j):
        k = 2*j - i
        if k < n:
            if A[i] == A[j]: continue
            if A[i] == A[k]: continue
            if A[k] == A[j]: continue
            ans -= 1
print(ans)

