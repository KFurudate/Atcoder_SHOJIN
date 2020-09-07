n = int(input())
ans = 10**18
for a in range(1, n):
    if n%a == 0:
      b = n//a
      ans = min(ans, a+b-2)
    elif a >= n**0.5:
        break
print(ans)