n = int(input())
num_list = input()

ans = 0
for i in range(n):
    ans += int(num_list[i-1])

print(ans)