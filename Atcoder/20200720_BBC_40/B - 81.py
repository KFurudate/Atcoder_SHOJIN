n = int(input())

for i in range(1, 10):
    tmp = (n / i)
    if tmp.is_integer() and 1<=tmp and tmp <=9:
        print("Yes")
        exit()
print("No")