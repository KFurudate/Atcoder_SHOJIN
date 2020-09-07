S = input()
T = input()

Counts = []
for i in range(len(S)-len(T)+1):
    cnt = 0
    Q = S[i:i + len(T)]
    for j in range(len(T)):
        if T[j] == Q[j]:
            cnt += 1
    Counts.append(cnt)

ans = len(T) - max(Counts)
print(ans)