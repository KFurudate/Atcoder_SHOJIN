#https://atcoder.jp/contests/abc076/tasks/abc076_c
# breakでループを抜けなかったときにのみ、elseが実行される

S = input()
T = input()
ls, lt = len(S), len(T)

ans = 'UNRESTORABLE'
for i in range(ls - lt + 1):
    for j in range(lt):
        if S[i + j] not in (T[j], '?'):
            break
    else:
        ans = (S[:i] + T + S[i + lt:]).replace('?', 'a')

print(ans)