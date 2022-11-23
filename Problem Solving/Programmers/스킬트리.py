# https://school.programmers.co.kr/learn/courses/30/lessons/49993#fn1

def solution(skill, skill_trees):
    answer = 0
    skill_dict = {}

    for i, s in enumerate(skill):
        skill_dict[s] = i

    for skill_tree in skill_trees:
        i = 0
        for user_skill in skill_tree:
            try:
                seq = skill_dict[user_skill]
            except:
                continue
            if seq > i:
                break
            i += 1
        else:
            answer += 1

    return answer


skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
