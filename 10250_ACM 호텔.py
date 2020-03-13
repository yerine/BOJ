t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    print("%s%02d"%(((n-1)%h+1,(n-1)//h+1)))