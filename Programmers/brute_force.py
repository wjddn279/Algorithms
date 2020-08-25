

def soluti(answers):
    answer = []
    dic = [0,0,0]
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    for idx,ans in enumerate(answers):
        if one[idx%5] == ans:
            dic[0] += 1
        if two[idx%8] == ans:
            dic[1] += 1
        if three[idx%10] == ans:
            dic[2] += 1
    max_val = max(dic)
    for idx,val in enumerate(dic):
        if val == max_val:
            answer.append(idx+1)
    return answer

from itertools import permutations


def isprime(a):
    if a == 0 or a == 1:
        return False
    for i in range(2,a):
        if a%i == 0:
            return False
    return True
def solution(numbers):
    data = list(numbers)
    dic = {}
    for i in range(1,len(data)+1):
        can = set(permutations(data,i))
        for nums in can:
            temp = ''
            for num in nums:
                temp += num
            if isprime(int(temp)):
                dic[int(temp)] = 0
    return len(dic)

def solutio(brown, yellow):
    limit = brown//2 + 2
    width, height = limit-2,2
    while width >= height:
        if width * height - brown == yellow:
            return [width,height]
        else:
            width -= 1
            height += 1



print(solution("17"))