#WA（たぶん割り算の切り捨てがあるから？）
import math
x = int(input())

#x = 100*(1.01**y)
#log10(x) = log10(100*(1.01**y))
#log10(x) = log10(100) + log10(1.01**y)
#log10(x) = 2 + y*log10(1.01)
#log10(x)-2 = y*log10(1.01)
#y = (log10(x)-2)//log10(1.01)

if x >= 1000:
  y = (math.log10(x)-1.75) // math.log10(1.01)
  print(int(y))
else:
  for i in range(1, 1001):
    if 100*(1.01**i) >= x:
      print(i)
      break
##############################

x = int(input())
ans = 0
a = 100
while a < x:
  a += a//100
  ans += a

print(ans)