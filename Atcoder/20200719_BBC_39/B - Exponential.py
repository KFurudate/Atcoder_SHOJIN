x = int(input())

ans = 0
tmp = 1
for i in range(1, int(x**0.5)+1):
    for j in range(2, x):
      tmp = pow(i, j)
      if tmp > x:
          tmp = pow(i, j-1)
          #print(tmp, i, j)
          break

    ans = max(tmp, ans)

print(ans)