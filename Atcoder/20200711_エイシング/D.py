def popcnt1(n):
    return bin(n).count("1")

n = int(input())
x = int(input())

for _ in range(n):
    print(popcnt1(x))