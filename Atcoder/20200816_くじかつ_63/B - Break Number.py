n = int(input())

for i in range(6, -1, -1):
    tmp = 2**i
    if n >= tmp:
      print(tmp)
      exit()