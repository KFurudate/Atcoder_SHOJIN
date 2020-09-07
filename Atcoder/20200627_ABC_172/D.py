# http://sucrose.hatenablog.com/entry/2016/11/06/234635
#　約数　高速

n = int(input())

def num_divisors_table(n):
    table = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            table[j] += 1

    return table

fk = num_divisors_table(n + 1)

ans = 0
for k in range(1, n + 1):
    ans += k * fk[k]

print(ans)

