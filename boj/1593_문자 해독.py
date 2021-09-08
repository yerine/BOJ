#import sys
#input = sys.stdin.readline

g, len_S = map(int, input().split())
W = input()
S = input()

answer =  0
W_list = [0] * 52
S_list = [0] * 52

for w in W:
    if 'A' <= w <= 'Z':
        W_list[ord(w) - ord('A')] += 1
    else:
        W_list[ord(w) - ord('a')+26] += 1

for i in range(g):
    w = S[i]
    if 'A' <= w <= 'Z':
        S_list[ord(w) - ord('A')] += 1
    else:
        S_list[ord(w) - ord('a')+26] += 1
    if S_list == W_list:
        answer += 1  

for i in range(g, len_S):
    w = S[i-g]
    if 'A' <= w <= 'Z':
        S_list[ord(w) - ord('A')] -= 1
    else:
        S_list[ord(w) - ord('a')+26] -= 1
    w = S[i]
    if 'A' <= w <= 'Z':
        S_list[ord(w) - ord('A')] += 1
    else:
        S_list[ord(w) - ord('a')+26] += 1
    if S_list == W_list:
        answer += 1    

print(answer)

