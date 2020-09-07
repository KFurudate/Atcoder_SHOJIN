a = input()

for i in range(2, 100):
    tmp = int(a, i)
    if tmp % 2==0:
        print(tmp)
        exit()

###############
a = input()

import string

numbers = "0123456789"
alphabets = string.ascii_letters  # a-z+A-Zをロード
characters = numbers + alphabets


def base_cvt(value, n=2):
    try:
        tmp = int(value)
    except:
        raise ValueError('Invalid value:', value)

    if n < 2 or n > len(characters):
        raise ValueError('Invalid n:', value)

    result = ''
    tmp = int(value)
    while tmp >= n:
        idx = tmp % n
        result = characters[idx] + result
        tmp = int(tmp / n)
    idx = tmp % n
    result = characters[idx] + result
    return result


for i in range(2, 63):
    tmp = base_cvt(a, i)
    if str(i) == tmp:
        print(i)
        exit()
print(-1)
###############
a = int(input())

def change(N,shinsu):
    keta=0
    for i in range(10**9):
        if N<shinsu**i:
             keta+=i
             break
    ans=[0]*keta
    check=0
    for i in range(1,keta+1):
        j=N//(shinsu**(keta-i))
        ans[check]=j
        check+=1
        N-=(j)*(shinsu**(keta-i))
    return ans

for i in range(2, 63):
    tmp = change(a, i)
    if str(i) == tmp:
        print(i)
        exit()
print(-1)





