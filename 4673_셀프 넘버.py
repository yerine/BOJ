def d(n):
    result = n
    while n > 0:
        result += (n%10)
        n //= 10
    return result

# 방법1
    
non_self = set()
for num in range(10000):
    non_self.add(d(num))
    min_non = min(non_self)
    if min_non <= num:
        non_self.remove(min_non)
    else:
        print(num)

# 방법2   
        
self_num = [0]*10000
for i in range(10000):
    d_num = d(i+1)
    if d_num-1 < 10000:
        if self_num[d_num-1] == 0:
            self_num[d_num-1] = 1        

for i in range(10000):
    if self_num[i] == 0:
        print(i+1)