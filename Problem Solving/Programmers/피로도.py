from itertools import permutations


def solution(k, dungeons):
    answer = -1
    full_search = list(permutations(range(len(dungeons)), len(dungeons)))

    for search in full_search:
        tired = k
        numbers_of_visited_dungeons = 0
        for index_of_dungeon in search:
            expect_tired, using_tired = dungeons[index_of_dungeon]
            if tired < expect_tired:
                break
            tired -= using_tired
            numbers_of_visited_dungeons += 1
        answer = max(answer, numbers_of_visited_dungeons)

    return answer


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution(k, dungeons))
