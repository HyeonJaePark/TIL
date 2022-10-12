from collections import defaultdict


def solution(genres, plays):
    answer = []
    genres_dict = defaultdict(list)
    genres_play = dict((key, 0) for key in set(genres))
    for i in range(len(plays)):
        genres_dict[genres[i]].append([i, plays[i]])
        genres_play[genres[i]] += plays[i]
    for i in genres_dict:
        genres_dict[i].sort(key=lambda x: (-x[1], x[0]))

    genres_play = {k: v for k, v in sorted(
        genres_play.items(), key=lambda item: -item[1])}

    for i in genres_play:
        if len(genres_dict[i]) > 1:
            answer.append(genres_dict[i][0][0])
            answer.append(genres_dict[i][1][0])
        elif len(genres_dict[i]) == 1:
            answer.append(genres_dict[i][0][0])

    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))
