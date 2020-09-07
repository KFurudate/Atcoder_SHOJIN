n = int(input())
L = list(map(int, input().split()))
cnt = 0
for i in range(n-2):
    print(i)
    for j in range(i+1,n-1):
        if L[i] == L[j]:continue
        for k in range(j+1,n):
            print(L[i], L[j], L[k], "*")
            if ((L[i] != L[k]) and (L[j] != L[k])) and ((L[i]+L[j]>L[k]) and (L[i]+L[k]>L[j]) and (L[j]+L[k]>L[i])):
              print(L[i], L[j], L[k])
              cnt += 1
print(cnt)