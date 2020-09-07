S = 'issii'
K = 2

#S = input()
#K = int(input())
T=S
count = 0
for i in range(len(T)-1):
    j = i+1
    check_list =[]
    if T[i] == T[j]:
        check_list.append(T[j])
    N = len(check_list)
    print(check_list)
    for i in range(N//2):
        count += 1
print(count*K)