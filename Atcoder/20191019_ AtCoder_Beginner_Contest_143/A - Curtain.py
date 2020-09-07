A, B = input().split()
A = int(A)
B = int(B)


if (B*2) >= A:
    print(0)
else:
    print(A-(B*2))

*******************
print(max(A-(B*2), 0))