A = int(input())
B = int(input())
C = int(input())
x = int(input())

cnt = 0
for a in range(A):
    for b in range(B):
        for c in range(C):
           if x == 500*a + 100*b + 50*c:
               cnt += 1

print(cnt)

