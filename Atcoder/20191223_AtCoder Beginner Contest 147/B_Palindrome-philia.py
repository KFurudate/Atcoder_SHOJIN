S = input()

x = len(S)//2
S_1 = S[:x]
S_2 = S[x:]
S_3 = S_2[::-1]

cont = 0
for i in range(x):
  if S_1[i] != S_3[i]:
    cont += 1
print(cont)