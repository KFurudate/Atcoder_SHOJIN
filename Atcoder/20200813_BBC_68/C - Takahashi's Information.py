C = [list(map(int, input().split())) for _ in range(3)]

# a1=0と仮定すると、b1=C[0][0], b2=C[0][1], b3=C[0][2]
# a2 = C[1][0]-b1 = C[1][1]-b2 = C[1][2]-b3
# a3 = C[2][0]-b1 = C[2][1]-b2 = C[2][2]-b3

b1, b2, b3 = C[0][0], C[0][1], C[0][2]
if (C[1][0]-b1 == C[1][1]-b2 == C[1][2]-b3) and (C[2][0]-b1 == C[2][1]-b2 == C[2][2]-b3):
    print("Yes")
else:
    print("No")