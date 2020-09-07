a, b, c, d = map(int, input().split())

if (d < abs(a-c)):
  if(d < abs(a-b) or d < abs(b-c)):
    print("No")
  else:
    print("Yes")
else:
  print("Yes")
