n, k = map(int, input().split())

ans = 0
while n > 0:
  n //= k
  ans += 1

print(ans)

#################
#ある数nのk進数を求める場合は、余りをリストにappendしていく
n, k = map(int, input().split())

#ans = 0
d = []
while n > 0:
  d.append(n%k)
  n //= k
  #ans += 1

#print(ans)
print(d)
