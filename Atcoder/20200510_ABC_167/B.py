a, b, c, k = map(int, input().split())

if k-a <= 0:
    print(k)

elif k-(a+b) <= 0:
    print(a)

elif k-(a+b) > 0:
  print(a-(k-(a+b)))

