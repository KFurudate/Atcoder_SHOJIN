n = int(input())
t, a = map(int, input().split())
H = list(map(int, input().split()))

Palace = []

for h in H:
    Palace.append(abs((t - h * 0.006) - a))

print(Palace.index(min(Palace))+1)