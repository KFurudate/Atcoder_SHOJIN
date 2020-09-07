#何が悪かったのか？？？順番と処理
A = input()
B = input()
C = input()


order = A[0]
A = A[1:]

while True:
    if order == "a":
        if A == "":
            print('A')
            exit()
        order = A[0]
        A = A[1:]

    if order == "b":
        if B == "":
            print('B')
            exit()
        order = B[0]
        B = B[1:]

    if order == "c":
        if C == "":
            print('C')
            exit()
        order = C[0]
        C = C[1:]
