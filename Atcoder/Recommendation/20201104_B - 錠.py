a = input()
b = input()

a_ = "1" + a
b_ = "1" + b

a, b = int(a), int(b)
a_, b_ = int(a_), int(b_)

ans = min(abs(a-b), abs(a_-b), abs(a-b_), abs(a_-b_))
print(ans)