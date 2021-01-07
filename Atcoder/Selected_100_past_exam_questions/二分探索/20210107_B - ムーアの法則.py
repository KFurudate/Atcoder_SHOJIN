# https://qiita.com/ganariya/items/1553ff2bf8d6d7789127
p = float(input())

#目的関数（最小化したい）
def f(x):
    return x + p / pow(2, (x/1.5))

left, right = 0, 100

while right - left > 0.000000001:
    mid_left = (left*2 + right)/3
    mid_right = (right*2 + left)/3

    if f(mid_right) >= f(mid_right):
        left = mid_left
    else:
        right = mid_right

print(f(left))