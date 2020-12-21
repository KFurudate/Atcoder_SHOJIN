n = int(input())

cnt = 0
lst = []
for i in range(1, n + 1):
    if "7" in oct(i):
        lst.append(i)
    elif "7" in str(i):
        lst.append(i)

print(n-len(lst))