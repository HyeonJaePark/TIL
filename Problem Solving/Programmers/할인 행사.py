# https://school.programmers.co.kr/learn/courses/30/lessons/131127

def init_dict(want, number):
    want_dict = {}

    for i, product in enumerate(want):
        want_dict[product] = number[i]

    return want_dict


def get_all_wants(want_dict):
    for x in list(want_dict.values()):
        if int(x) > 0:
            break
    else:
        return 1

    return 0


def exclude_oldest_product(day, discount, want_set, want_dict):
    if discount[day] in want_set:
        want_dict[discount[day]] += 1

    return want_dict


def include_newest_product(day, discount, want_set, want_dict):
    if discount[day] in want_set:
        want_dict[discount[day]] -= 1

    return want_dict


def solution(want, number, discount):
    answer = 0
    window_size = 10

    want_dict = init_dict(want, number)
    want_set = set(want_dict.keys())

    for day in range(window_size):
        want_dict = include_newest_product(day, discount, want_set, want_dict)

    answer += get_all_wants(want_dict)

    new = 10
    far = 0
    while new < len(discount):
        want_dict = exclude_oldest_product(far, discount, want_set, want_dict)
        want_dict = include_newest_product(new, discount, want_set, want_dict)

        answer += get_all_wants(want_dict)

        new += 1
        far += 1

    return answer


want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple",
            "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))


# def solution(want, number, discount):
#     answer = 0
#     window_size = 10
#     want_dict = {}

#     for i, product in enumerate(want):
#         want_dict[product] = number[i]

#     want_set = set(want_dict.keys())

#     for i in range(window_size):
#         if discount[i] in want_set:
#             want_dict[discount[i]] -= 1

#     for i in list(want_dict.values()):
#         if int(i) > 0:
#             break
#     else:
#         answer += 1


#     i = 10
#     j = 0
#     while i < len(discount):
#         if discount[j] in want_set:
#             want_dict[discount[j]] += 1
#         if discount[i] in want_set:
#             want_dict[discount[i]] -= 1

#         for x in list(want_dict.values()):
#             if int(x) > 0:
#                 break
#         else:
#             answer += 1

#         i += 1
#         j += 1

#     return answer
