n = int(input())
T = sorted([int(input()) for _ in range(n)])

H = [i + 1 for i in range(2 * n)]
H = list(set(T) ^ set(H))
# print(T)
# print(H)

if T[1] > H[0]:
    ans = T[0] - 1
    if T[1] - T[0] > 2:
        ans += T[1] - T[0] - 2
    print(ans)
    print(0)
else:
    ans = H[0] - 1
    if H[1] - H[0] > 2:
        ans += H[1] - H[0] - 2
    print(0)
    print(ans)

#############################################
n = int(input())
T = sorted([int(input()) for _ in range(n)])
taro = [0]*(2*n)
hana = [1]*(2*n)
for t in T:
    taro[t-1] = 1
    hana[t-1] = 0

print(taro)
print(hana)

ans_T, ans_H = n, n

