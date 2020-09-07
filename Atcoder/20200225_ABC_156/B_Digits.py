n, k = map(int, input().split())
#n進数表記
#http://iatlex.com/python/base_change
def base_to_n(x,n):
    if(int(x/n)):
        return base_to_n(int(x/n), n)+str(x%n)
    return str(x%n)

print(len(base_to_n(n,k)))