n = int(input())

idx=0
while idx < n:
  idx += 10
idx*=10

ans = min(15*n, 15*(n%10)+(n//10*100), idx)
print(ans)
