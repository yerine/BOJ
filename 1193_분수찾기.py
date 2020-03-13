x = int(input())

n = 0
i = 1
while n < x:
    n += i
    i += 1

if i % 2 == 0:
    print("%s/%s"%(n-x+1,i-n+x-1))
else:
    print("%s/%s"%(i-n+x-1,n-x+1))