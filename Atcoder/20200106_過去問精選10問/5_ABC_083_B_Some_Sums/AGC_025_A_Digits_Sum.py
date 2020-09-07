n = int(input())

def Checker(sum, x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

sum_list = []
for a in range(1, n):
    b = n - a
    sum_a = 0
    sum_b = 0

    y = Checker(sum_a, a)+ Checker(sum_b, b)
    sum_list.append(y)

print(min(sum_list))