S = input()
cnt = (len(S)-1)*2
for i in range(1, len(S)-1):
    if S[i] == "U":
        cnt += i*2
        cnt += len(S)-2-i
    if S[i] == "D":
        cnt += i
        cnt += (len(S)-2-i)*2
print(cnt)
