a = [100, 100, 200]

n = 19
for i in range(n-2):
  tmp = 0
  tmp += a[i]
  tmp += a[i+1]
  tmp += a[i+2]
  a.append(tmp)

print(a[-1])