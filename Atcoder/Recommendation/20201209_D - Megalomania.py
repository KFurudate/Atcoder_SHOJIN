n = int(input())
AB = [list(map(int, input().split())) for _ in range(n)]
BA = sorted([(b, a) for a, b in AB])

ans = 0
for b, a in BA:
  ans += a
  if ans > b:
    print("No")
    exit()
print("Yes")
