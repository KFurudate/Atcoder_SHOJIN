import string

S = list(input())
set_S = set(S)

a2z = list(string.ascii_lowercase)
check = [i for i in a2z if i not in set_S]

if check:
    check = sorted(check)
    print(check[0])
else:
    print('None')