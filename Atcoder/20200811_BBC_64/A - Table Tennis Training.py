n, a, b = map(int, input().split())

if a == b+1:
    ans = b

else:
    if (b-a) %2:
        ans = (b-a)//2 +1
    else:
        ans = (b-a)//2
print(ans)
