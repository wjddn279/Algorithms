def solution(record):
    answer = []
    dic = {}
    # change, leave, enter
    for rec in record:
        arr = rec.split(' ')
        if len(arr) == 3:
            com,id,name = arr
            dic[id] = name

    for rec in record:
        arr = rec.split(' ')
        if arr[0] == 'Enter':
            answer.append(dic[arr[1]]+"님이 들어왔습니다.")
        elif arr[0] == 'Leave':
            answer.append(dic[arr[1]]+"님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
