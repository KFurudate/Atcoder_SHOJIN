def f(x):
    if x == 1:
        return 1
    return f(x//2)*2+1

h = int(input())
print(f(h))