h, m = map(int, input().split())
A = sum(list(map(int, input().split())))

if h >= A:
    print("Yes")
else:
    print("No")

