a = int(input())

def Conv_N_base(n, base):
    digit = 0
    for i in range(10**9):
        if n < base**i:
            digit += i
            break
    ans = [0]* digit
    idx = 0
    for i in range(1, digit+1):
        j = n // (base**(digit-i))
        ans[idx] = str(j)
        idx += 1
        n -= j * (base**(digit-i))
    return ans

for i in range(2, 10001):
    tmp = Conv_N_base(a, i)
    if str(i) == (''.join(tmp)):
        print(i)
        exit()
print(-1)
