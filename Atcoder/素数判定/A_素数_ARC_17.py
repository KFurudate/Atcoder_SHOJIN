#https://atcoder.jp/contests/arc017/tasks/arc017_1
#素数判定

def is_prim(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True

n = int(input())

if is_prim(n):
    print('YES')
else:
    print('NO')
