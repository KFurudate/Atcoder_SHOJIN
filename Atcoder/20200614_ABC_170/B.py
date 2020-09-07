X,Y = map(int, input().split())

if Y < 4*X and Y % 2 == 0 and Y > 2*X:
    print("Yes")
else:
    print("No")

###################
X, Y = map(int, input().split())

for i in range(101):
    for j in range(101):
        if (2 * i + 4 * j == Y) and (i + j == X):
            print("Yes")
            exit()
print("No")
