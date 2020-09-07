a, b, c, d = map(int, input().split())

T_hp = a
A_hp = c
for _ in range(100):
    A_hp -= b
    if A_hp <= 0:
        print('Yes')
        exit()
    T_hp -= d
    if T_hp <= 0:
        print('No')
        exit()