def solution(gems):
    min_length = float('inf')
    answer,dic = [1,1],{}
    total = len(gems)
    # 같으면 시작 구간이 작은 진열대 번호 부터
    for gem in gems:
        if gem not in dic:
            dic[gem] = 0
    left,right = 0 ,0
    dic[gems[0]] = 1
    temp = [gems[0]]
    while right < total-1 and left < total-1:
        if right == total -1:
            if len(temp) == len(dic) and (right - left) < min_length:
                answer = [left + 1, right + 1]
                min_length = right - left
            dic[gems[left]] -= 1
            if dic[gems[left]] == 0:
                temp.remove(gems[left])
            left += 1
        elif left == right:
            right += 1
            dic[gems[right]] += 1
            if dic[gems[right]] == 1:
                temp.append(gems[right])
            continue
        else:
            if len(temp) == len(dic):
                if (right-left) < min_length:
                    answer = [left+1,right+1]
                    min_length = right-left
                dic[gems[left]] -= 1
                if dic[gems[left]] == 0:
                    temp.remove(gems[left])
                left += 1
            else:
                right += 1
                dic[gems[right]] += 1
                if dic[gems[right]] == 1:
                    temp.append(gems[right])
    return answer


print(solution(["AA","AB","CC","AA","AA","CC","DD","AB"]))