n = int(input())
A = list(map(int, input().split()))

A_set = list(set(A))

if len(A) == len(A_set):
    print("YES")

else:
    print("NO")