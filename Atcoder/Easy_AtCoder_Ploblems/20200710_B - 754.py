S = input()

ans = 753- int(S[:3])
for i in range(1, len(S)-1):
    tmp = int(S[i:i+3])
    ans = min(abs(753-tmp), ans)

print(ans)