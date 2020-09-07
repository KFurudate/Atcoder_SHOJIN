S = input()
T = input()

if len(set(S)) != len(set(T)):
    print("No")
    exit()
else:
    for i in range(len(S)):
        if S.index(S[i]) != T.index(T[i]):
            print("No")
            #print(S.index(S[i]), T.index(T[i]))
            exit()
print("Yes")