N = int(input())

def Checker(N):
  for A in range(1, 10):
    for B in range(1, 10):
      if A*B == N:
        print('Yes')
        return 0
  print('No')

Checker(N)