#H = int(input())
H = 8
def f(x):
    if x == 1:
        return 1
    return f(x//2)*2+1

print(f(H))