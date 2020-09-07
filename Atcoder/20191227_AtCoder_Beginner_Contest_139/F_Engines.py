S = input()
T = input()

n = len(S)
cont = 0
for i in range(n):
    if S[i] == T[i]:
        cont += 1
print(cont)