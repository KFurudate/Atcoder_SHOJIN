k = int(input())

if k % 2 == 0:
    print(-1)
    exit()

tmp = str(7)
for i in range(2, 10 ** 5 + 1):
    if int(tmp) % k == 0:
        print(i-1)
        exit()
    tmp *= i
###############################
#tmp = str(7)*999982
#print(int(tmp)%999983)

k = int(input())

if k % 2 == 0:
    print(-1)
    exit()


###############################
