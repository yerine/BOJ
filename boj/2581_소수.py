# 방법1
m = int(input())
n = int(input())

prime_sum = 0
while n >= m:
    prime = True
    if n == 1:
        prime = False
    else:
        for j in range(2, n):
            if n % j == 0:
                prime = False
                break
            
    if prime == True:
        prime_sum += n
        prime_min = n
        
    n -= 1
    
if prime_sum == 0:
    print(-1)
else:
    print(prime_sum)
    print(prime_min)
    
# 방법2
m = int(input())
n = int(input())

arr = [False] + [True]*(n-1)

for i in range(2, int(n**0.5 + 1)):
    if arr[i-1]:
        for j in range(i*2,n+1,i):
            arr[j-1] = False

prime_list = [i for i in range(m,n+1) if arr[i-1]]

if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list))
    print(prime_list[0])