def solution(survey, choices):
    answer = ''
    dir = ['RT', 'CF', 'JM', 'AN']
    score = {'A': 0, 'N': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'R': 0, 'T': 0}

    for i in range(len(survey)):
        if choices[i] < 4:
            score[survey[i][0]] += abs(choices[i] % -4)
        else:
            score[survey[i][1]] += choices[i] % 4
        print(score)

    for i in range(4):
        left, right = dir[i][0], dir[i][1]
        if score[left] >= score[right]:
            answer += left
        else:
            answer += right

    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))
