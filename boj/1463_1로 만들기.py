#벙법1
n = int(input())

lst = [0,0,1,1]
for i in range(4,n+1):
    temp = [lst[i-1]]
    if i % 2 == 0:
        temp.append(lst[int(i/2)])
    if i % 3 == 0:
        temp.append(lst[int(i/3)])

    lst.append(min(temp)+1)

print(lst[n])
lst[1:]

#방법2