l, r = map(int, input().split())
def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a%b)

x = gcd(l*r, 2019)
y = divmod(l*r, 2019)[1]

for i in range(y+1):
    q, mod = divmod(i, 2019)
    if q == x:
        print(i)
        exit()

##########################
l, r = map(int, input().split())
def gcd(a, b):
  if b == 0:
    return a
  return gcd(b, a%b)

x = gcd(l*r, 2019)
y = divmod(l*r, 2019)[1]
for i in range(y+1):
    if gcd(i, 2019) == x:
      ans = min(y, i)
print(ans)



