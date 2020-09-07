"""
'S'=晴
'C'=曇
'R'=雨
3日間で天気予報が的中した日が何日あるかを出力せよ。

入力
CSS
CSR

出力
2
"""

#S= ['C', 'S', 'S']
#T= ['C', 'S', 'R']

S= input()
T= input()

S_list = []
T_list = []
def split_lint(text, list):
    words=text.split()
    for word in words:
        list.append(word)
split_lint(S, S_list)
split_lint(T, T_list)

count=0
for i in range(3):
    if S_list[i] == T_list[i]:
       count += 1
print(count)