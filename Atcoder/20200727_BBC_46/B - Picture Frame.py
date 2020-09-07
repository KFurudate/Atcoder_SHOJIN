h, w = map(int, input().split())
img = [input() for i in range(h)]


for i in range(h):
    if i==0:
        print("#"*(w+2))
    print("#"+img[i]+"#")
print("#"*(w+2))
