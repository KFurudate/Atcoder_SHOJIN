n = input()

SUM_odd = 0
for i in range(-1, -len(n)-1, -2):
  SUM_odd += int(n[i])

SUM_evn = 0
for j in range(-2, -len(n)-1, -2):
   SUM_evn += int(n[j])
print(SUM_evn, SUM_odd)