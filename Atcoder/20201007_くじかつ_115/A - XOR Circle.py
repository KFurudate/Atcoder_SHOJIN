from collections import Counter

n = int(input())
A = list(map(int, input().split()))
C = Counter(A)

if len(C) == 1 and 0 in A:
    print("Yes")
    exit()

elif len(C) == 2 and n%3 == 0:
    for k, v in C.items():
        if k == 0 and v == n // 3:
            print("Yes")
            exit()

elif len(C) == 3 and n%3 == 0:
    A_s = list(set(A))
    init = A_s[0]
    x = A_s[1] ^ A_s[2]
    if x == init:
        t = None
        for v in C.values():
            if t is None:
                t = v
            else:
                if t != v:
                    break
        else:
            print("Yes")
            exit()
print("No")

