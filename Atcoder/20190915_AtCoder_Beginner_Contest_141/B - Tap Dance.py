#S = 'RUDLUDR'
#S ='DULL'
#S ='UUUUUUUUUUUUUUU'

S = input()
odd_S = []
even_S = []

for i in range(0, len(S), 2):
    odd_S.append(S[i])

for j in range(1, len(S), 2):
    even_S.append(S[j])

if ['L'] not in odd_S and ['R'] not in even_S:
    print('Yes')
else:
    print('No')


""""
問題文
高橋君はタップダンスをすることにしました。タップダンスの動きは文字列 
S
 で表され、
S
 の各文字は L, R, U, D のいずれかです。各文字は足を置く位置を表しており、
1
 文字目から順番に踏んでいきます。

S
 が以下の 
2
 条件を満たすとき、またその時に限り、
S
 を「踏みやすい」文字列といいます。

奇数文字目がすべて R, U, D のいずれか。
偶数文字目がすべて L, U, D のいずれか。
S
 が「踏みやすい」文字列なら Yes を、そうでなければ No を出力してください。

制約
S
 は長さ 
1
 以上 
100
 以下の文字列
S
 の各文字は L, R, U, D のいずれか
"""