n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = sum(B)

tmp = A[0]
for a in A[1:]:
    if a == tmp+1:
        ans += C[a-2]
    tmp = a

print(ans)
