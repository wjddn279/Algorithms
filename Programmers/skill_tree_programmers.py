# def solution(skill, skill_trees):
#     answer = 0
#     dic = {}
#     for idx,sk in enumerate(skill):
#         dic[sk] = idx
#     for skill_tree in skill_trees:
#         num = -1
#         for alpha in skill_tree:
#             if alpha in dic:
#                 if num == -1 and dic[alpha] != 0:
#                     break
#                 if dic[alpha] == num+1:
#                     num = dic[alpha]
#                 else:
#                     break
#         else:
#             answer += 1
#     return answer


def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        temp = []
        for s in skill:
            try:
                temp.append(tree.index(s))
            except:
                temp.append(len(tree)+1)
        if temp == sorted(temp):
            answer += 1

    return answer


print(solution("BDC",["AAAABACA"]))