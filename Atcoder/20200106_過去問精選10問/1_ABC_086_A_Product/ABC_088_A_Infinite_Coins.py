N = input()
A = int(input())
n = int(N)
x = 0

if n > 100:
    x = int(N[-3])
    if x >= 5:
        x = x - 5

y = int(N[-2])
z = int(N[-1])
X = (x * 100) + (y * 10) + z

if n <= A or X <= A:
    print('Yes')
else:
    print('No')


##################

N = int(input())
A = int(input())

if N%500 <= A:
    print('Yes')
else:
    print('No')
