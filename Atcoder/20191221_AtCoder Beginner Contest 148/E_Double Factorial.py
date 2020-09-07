n = int(input())

def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x - 2)

print(fact(n))

#末尾に0が生じるのは素因数に2と5が一つずつ登場した場合

n = int(input())


def factorial_cor(n):
    fact = 1
    for integer in range(1, n + 1, 2):
        fact *= integer
    return fact

factorial_cor(n)


def factorization(n):
    arr = []
    temp = n
    count = 0
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
            if i == 5:
                count += 1
    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return count


print(factorization(fact(n)))

n = int(input())


def factorial_cor(n):
    fact = 1
    for integer in range(1, n + 1, 2):
        fact *= integer
    return fact

def factorization(n):
    arr = []
    temp = n
    count = 0
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i

            if i == 5:
                count += 1

    return count


print(factorization(factorial_cor(n)))