n = int(input())

x_list = []
y_list = []
for _ in range(n):
    x, y = map(int, input().split())
    x_list.appned(x)
    y_list.append(y)

leng_list=[]
for i in range(n):
    j = i - 1
    leng_list.appned((x_list[i] - x_list[j])**2 + (y_list[i] - y_list[j])**2)

sum_list =[]
for i in range(n):
    j = i - 1
    sum_list.append(leng_list[i] + leng_list[j])


print(sum(sum_list)/n)


