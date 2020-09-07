n = int(input())
A = list(map(int, input().split()))
cont = 0
cont_list =[]

for a in A:
    if a % 2 != 0:
      cont_list.append(cont)
      break
    else:
        while a % 2==0:
            a //= 2
            cont += 1
        cont_list.append(cont)
        cont=0

print(min(cont_list))



