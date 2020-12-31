m, n = map(int, input().split())

prime_list = [False] + [True]*(n-1)

for i in range(2, int(n**0.5 + 1)):
    if prime_list[i-1]:
        for j in range(i*2,n+1,i):
            prime_list[j-1] = False

for i in range(m,n+1):
    if prime_list[i-1]:
        print(i)