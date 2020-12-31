def solution(phone_book):
    answer = True

    for i in range(len(phone_book)-1):
        for j in range(i+1,len(phone_book)):
            if len(phone_book[i]) <= len(phone_book[j]):
                if phone_book[j].startswith(phone_book[i]):
                    answer = False
                    return answer
            else:
                if phone_book[i].startswith(phone_book[j]):
                    answer = False
                    return answer

    return answer

#다른 사람의 풀이

def solution(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True