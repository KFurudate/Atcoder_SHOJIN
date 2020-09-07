n = int(input())
x_list = []
y_list = []
for _ in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

ans = []
for i in range(n):
    for j in range(n):
        if i != j:
            ans.append(((x_list[i]-x_list[j])**2 + (y_list[i]-y_list[j])**2)**0.5)

print(max(ans))