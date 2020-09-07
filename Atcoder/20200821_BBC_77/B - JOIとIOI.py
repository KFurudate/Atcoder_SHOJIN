S = input()

cnt1 = 0
cnt2 = 0
for i in range(len(S)-2):
  if S[i:i+3] == "JOI":
    cnt1 += 1
  if S[i:i+3] == "IOI":
    cnt2 += 1
print(cnt1)
print(cnt2)