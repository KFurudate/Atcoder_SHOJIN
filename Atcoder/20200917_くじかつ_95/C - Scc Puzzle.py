n, m = map(int, input().split())

if n >= m:
    print(m)
else:
    nx = (m-n)//3
    print(nx)


