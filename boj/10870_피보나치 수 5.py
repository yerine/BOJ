n = int(input())

lst = [0,1]

for i in range(n-1):
    lst.append(lst[-1]+lst[-2])
    
print(lst[n])