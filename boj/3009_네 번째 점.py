x_list = []
y_list = []

for i in range(3):
    x, y = map(int, input().split())
    
    x_list.append(x)
    y_list.append(y)
    
for i in set(x_list):
    if x_list.count(i) == 1:
        print(i, end = ' ')

for i in set(y_list):
    if y_list.count(i) == 1:
        print(i)