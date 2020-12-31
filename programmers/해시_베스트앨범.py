from operator import itemgetter

def solution(genres, plays):
    answer = []

    genre_rank = {}
    for i in range(len(genres)):
        genre_rank[genres[i]] = genre_rank.get(genres[i],[0,{}])
        genre_rank[genres[i]][0] += plays[i]
        genre_rank[genres[i]][1][i] = plays[i]
    genre_rank = sorted(genre_rank.items(),key=itemgetter(1),reverse=True)

    for genre, cnt in genre_rank:
        play_rank = sorted(cnt[1].items(),key=itemgetter(1),reverse=True)
        if len(play_rank) == 1:
            answer.append(play_rank[0][0])
        else:
            answer.append(play_rank[0][0])
            answer.append(play_rank[1][0])
    return answer