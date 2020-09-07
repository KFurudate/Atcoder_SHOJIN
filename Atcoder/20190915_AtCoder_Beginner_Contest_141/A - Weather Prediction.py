"""
高橋君の住む町の天気は、一日ごとに晴れ(Sunny)、くもり(Cloudy)、雨(Rainy)、晴れ、くもり、雨、… と周期的に変化します。

今日の天気を表す文字列
S
 が与えられるので、明日の天気を予測してください。

制約
S
 は Sunny, Cloudy, Rainy のいずれかである
高橋君の住む町の天気は、一日ごとに晴れ(Sunny)、くもり(Cloudy)、雨(Rainy)、晴れ、くもり、雨、… と周期的に変化します。

今日の天気を表す文字列
S
 が与えられるので、明日の天気を予測してください。

制約
S
 は Sunny, Cloudy, Rainy のいずれかである

"""

S = 'Sunny'

S = input()
wether = ['Sunny', 'Cloudy', 'Rainy', 'Sunny']
pred = ''

for i in range(3):
    if S == wether[i]:
        pred = wether[i+1]
print(pred)



