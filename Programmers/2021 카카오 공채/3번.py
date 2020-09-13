import heapq

def solution(info, query):
    answer = []
    mapping = {'cpp':{'backend':{'junior':{'chicken':[],'pizza':[]},
                                 'senior':{'chicken':[],'pizza':[]}},
                      'frontend':{'junior':{'chicken':[],'pizza':[]},
                                  'senior':{'chicken':[],'pizza':[]}}},
               'java':{'backend':{'junior':{'chicken':[],'pizza':[]},
                                  'senior':{'chicken':[],'pizza':[]}},
                       'frontend':{'junior':{'chicken':[],'pizza':[]},
                                   'senior':{'chicken':[],'pizza':[]}}},
               'python':{'backend':{'junior':{'chicken':[],'pizza':[]},
                                    'senior':{'chicken':[],'pizza':[]}},
                         'frontend':{'junior':{'chicken':[],'pizza':[]},
                                     'senior':{'chicken':[],'pizza':[]}}}}
    for row in info:
        lan,pos,lv,food,score = row.split()
        mapping[lan][pos][lv][food].append(int(score))
    for row in query:
        result = 0
        lan,pos,lv,food = row.split(" and ")
        food,score = food.split()
        if lan == '-':
            temp_lan = [i for i in mapping.values()]
        else:
            temp_lan = [mapping[lan]]
        temp_pos = []
        if pos == '-':
            for con in temp_lan:
                temp_pos.append(con['backend'])
                temp_pos.append(con['frontend'])
        else:
            for con in temp_lan:
                temp_pos.append(con[pos])
        temp_lv = []
        if lv == '-':
            for con in temp_pos:
                temp_lv.append(con['junior'])
                temp_lv.append(con['senior'])
        else:
            for con in temp_pos:
                temp_lv.append(con[lv])
        temp_food = []
        if food == '-':
            for con in temp_lv:
                temp_food.append(con['chicken'])
                temp_food.append(con['pizza'])
        else:
            for con in temp_lv:
                temp_food.append(con[food])
        temp = []
        for arr in temp_food:
            temp += arr
        temp.sort()
        left = 0
        right = len(temp) - 1
        while left <= right:
            mid = (left + right) // 2
            if int(temp[mid]) == int(score):
                print(mid + 1)
                break
            elif int(temp[mid]) > int(score):
                right = mid - 1
            else:
                left = mid + 1

        answer.append(len(temp)-mid)

    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))