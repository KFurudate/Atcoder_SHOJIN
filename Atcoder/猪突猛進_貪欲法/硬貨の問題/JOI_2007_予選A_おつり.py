#https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_a
n = int(input())

cha = 1000 - n

cnt = 0
coi = [500, 100, 10, 5, 1]
for i in range(5):
    s = cha//coi[i]
    if s == 0: continue
    cnt = s
    cha = cha - coi[i]*s
    print(cha)

print(cnt)