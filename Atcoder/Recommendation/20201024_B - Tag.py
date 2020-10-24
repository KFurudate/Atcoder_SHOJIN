A, v = map(int, input().split())
B, w = map(int, input().split())
T = int(input())

if A == B:
    print("Yes")
    exit()

if w > v:
    print("NO")
    exit()

elif w == v and A != B:
    print("No")
    exit()

if A < B:
    if A+v*T >= B+w*T:
        print("YES")
    else:
        print("NO")

if A > B:
    if -A+v*T >= -B+w*T:
        print("YES")
    else:
        print("NO")


