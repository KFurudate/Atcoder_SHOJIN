n = int(input())
T = list(map(int, input().split()))
m = int(input())
PX = [map(int, input().split()) for _ in range(m)]

for p, x in PX:
    ans = sum(T)
    ans -= T[p-1]
    ans += x
    print(ans)