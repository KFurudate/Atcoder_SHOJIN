n, m = map(int, input().split())
A = [input() for _ in range(n)]
B = [input() for _ in range(m)]

print(A)
print(B)

for a in A:
    #print(a)
    for i in range(1, -2, -2):
        if i == 1:
            tmp = a[i:]
        else:
            tmp = a[:i]
        for b in B:
            flg = True
            if tmp != b:
                flg = False
            if flg:
                print("Yes")
                exit()
print("No")

#################
n, m = map(int, input().split())
A = [input() for _ in range(n)]
B = [input() for _ in range(m)]

print(A)
print(B)

for b in B:
    flg = True
    for a in A:
        if b not in a:

            flg = False
        if flg:
            print("Yes")
            exit()
print("No")

#################