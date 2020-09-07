n = int(input())
s = input()
t = input()

if s == t:
  ans = len(s)
  while ans < n:
    ans += 1
  print(ans)
  exit()

if len(set(s+t)) == (len(s)+len(t)):
    ans = len(s)+len(t)
    while ans < n:
        ans += 1
    print(ans)
    exit()

if (len(s)+len(t)) <= n:
    ans = len(s)+len(t)
    while ans < n:
        ans += 1
    print(ans)
    exit()

ans = len(s)+len(t)
for i in range(1, len(s)):
    if s[::-1][:i] == t[:i]:
        tmp = len(s)+len(t[i:])
        if tmp < n:
          break
        ans = min(ans, tmp)

print(ans)
