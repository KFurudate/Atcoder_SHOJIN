n = int(input())
cont = 0
cont_list = [1]

for i in range(2, n+1, 2):
    while i % 2 == 0:
        i //= 2
        cont += 1
    cont_list.append(cont)
    cont = 0

if max(cont_list) == 1:
    print(1)
else:
    print(2**(max(cont_list)))

##################
n = int(input())

ans = 1
while ans * 2 <= n:
    ans *= 2
print(ans)