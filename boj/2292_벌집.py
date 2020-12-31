n = int(input())

cnt = 1
location = 1
while n > location:
    cnt += 1
    location += 6*(cnt-1)
    
print(cnt)