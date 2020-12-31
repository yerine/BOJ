#import sys
#input = sys.stdin.readline

num = check = int(input())

cnt = 0
while 1:
    cnt += 1
    num_r = num%10   # 오른쪽 자릿수
    num_l = num//10  # 왼쪽 자릿수
    new = (num_r + num_l)%10 + num_r*10

    if check == new:
        break
    else:
        num = new
        
print(cnt)