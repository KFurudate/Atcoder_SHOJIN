N = list(input())

if len(N) == 1:
    ans = N[0]

elif (len(set(N)) == 1) and (list(set(N))[0] == "9"):
    ans = 9 * len(N)

else:
    tmp = 0
    for n in N:
        tmp += int(n)
    ans = max(tmp, (len(N) - 1) * 9 + int(N[0]) - 1)

print(ans)