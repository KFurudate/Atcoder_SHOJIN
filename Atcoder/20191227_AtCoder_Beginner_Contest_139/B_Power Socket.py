a, b = map(int, input().split())
if a >= b:
    print(1)
else:
    for i in range(2, 21):
      if (a*i) - (i-1) < b-1:
        continue
      else:
        break
    print(i)