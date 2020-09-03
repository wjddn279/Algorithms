from itertools import combinations

def checkmin(arr,brr):
    for num in brr:
        if num not in arr:
            return False
    else:
        return True
def solution(relation):
    answer = 0
    column = len(relation[0])
    combinate = []
    unique = []
    for r in range(column,0,-1):
        combinate += list(combinations(list(range(column)),r))
    for comb in combinate:
        temp = []
        for relate in relation:
            arr = [relate[num] for num in comb]
            if arr in temp:
                break
            else:
                temp.append(arr)
        else:
            unique.append(comb)
    for arr in unique:
        for brr in unique:
            if arr == brr:
               continue
            if checkmin(arr,brr):
                break
        else:
            answer += 1

    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))