a, b, c = map(int, input().split())

if a == b == c:
    print(-1)
    exit()

if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
    print(0)
    exit()

N = (a + b + c) // 3
cnt = 1
while N:
    if N % 2 != 0: break
    N //= 2
    cnt += 1

print(cnt)




