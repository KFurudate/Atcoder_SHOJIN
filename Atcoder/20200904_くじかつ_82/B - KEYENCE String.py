S = input()

for i in range(len(S)):
    for j in range(len(S)):
        if S[:j]+S[i:] == "keyence":
            print("YES")
            exit()
print("NO")